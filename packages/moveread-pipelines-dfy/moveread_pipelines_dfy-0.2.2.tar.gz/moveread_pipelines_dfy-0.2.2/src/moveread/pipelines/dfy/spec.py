from typing import TypedDict, Sequence, Any, Mapping, Coroutine, Protocol, Unpack, NotRequired
from dataclasses import dataclass, field
from haskellian import Iter, kwargs as kw
from pipeteer import Wrapped, Workflow
from dslog import Logger
from fastapi import FastAPI
from chess_pairings import GameId, gameId
import tf.serving as tfs
from moveread.pipelines.input_validation import InputValidation
import moveread.pipelines.preprocess as prep
from moveread.pipelines.game_preprocess import GamePreprocess, Params as GamepreParams
import moveread.pipelines.ocr_predict as ocr
import moveread.pipelines.game_correction as gamecorr

@dataclass
class BaseInput:
  title: str
  gameId: GameId
  serving_endpoint: str | None = field(default=None, kw_only=True)
  model: str
  imgs: Sequence[str]

class Input(BaseInput):
  ...

class PreprocessInput(BaseInput):
  ...

class InputVal(Wrapped[Input, Any, InputValidation.Input, InputValidation.Output, InputValidation.Queues, InputValidation.Params, InputValidation.Artifacts]):
  def __init__(self):
    super().__init__(Input, InputValidation())
  
  def pre(self, inp: Input) -> InputValidation.Input:
    return InputValidation.Input(gameId=inp.gameId, imgs=inp.imgs)
  
  def post(self, inp: Input, out: InputValidation.Output):
    gid = gameId(inp.gameId['tournId'], **out.gameId)
    title = inp.title if gid == inp.gameId else f'Changed to: {gid["group"]}/{gid["round"]}/{gid["board"]} from: {inp.gameId["group"]}/{inp.gameId["round"]}/{inp.gameId["board"]}'
    return PreprocessInput(gameId=gid, model=inp.model, imgs=out.imgs, title=title, serving_endpoint=inp.serving_endpoint)
  
@dataclass
class BasePreprocessed(BaseInput):
  ply_boxes: Sequence[Sequence[str]]
  preprocessed_imgs: Sequence[prep.Output]

class Preprocessed(BasePreprocessed):
  ...

class Preprocessing(Wrapped[PreprocessInput, Preprocessed, GamePreprocess.Input, GamePreprocess.Output, GamePreprocess.Queues, GamePreprocess.Params, GamePreprocess.Artifacts]):
  def __init__(self):
    super().__init__(PreprocessInput, GamePreprocess())
  
  def pre(self, inp: PreprocessInput):
    return GamePreprocess.Input(model=inp.model, imgs=inp.imgs)
  
  def post(self, inp: PreprocessInput, out: Sequence[prep.Output]) -> Preprocessed:
    ply_boxes = Iter(out) \
      .flatmap(lambda img: img.boxes) \
      .map(lambda box: [box]) \
      .sync() # OCR expects multiple boxes per ply
    return Preprocessed(preprocessed_imgs=out, gameId=inp.gameId, model=inp.model, imgs=inp.imgs, ply_boxes=ply_boxes, title=inp.title, serving_endpoint=inp.serving_endpoint)
  

@dataclass
class BasePredicted(BasePreprocessed):
  ocrpreds: ocr.Preds

class Predicted(BasePredicted):
  ...

class Prediction(Wrapped[Preprocessed, Predicted, ocr.Input, ocr.Preds, ocr.OCRPredict.Queues, ocr.Params, Coroutine]):
  def __init__(self):
    super().__init__(Preprocessed, ocr.OCRPredict())
  
  def pre(self, inp: Preprocessed):
    return ocr.Input(ply_boxes=inp.ply_boxes, endpoint=inp.serving_endpoint)
  
  def post(self, inp: Preprocessed, out: ocr.Preds) -> Predicted:
    return Predicted(gameId=inp.gameId, model=inp.model, imgs=inp.imgs, ply_boxes=inp.ply_boxes, preprocessed_imgs=inp.preprocessed_imgs, ocrpreds=out, title=inp.title, serving_endpoint=inp.serving_endpoint)
  

@dataclass
class Output(BasePredicted, gamecorr.CorrectResult):
  ...

class Correction(Wrapped[Predicted, Any, gamecorr.Input, gamecorr.Output, gamecorr.GameCorrection.Queues, gamecorr.GameCorrection.Params, gamecorr.GameCorrection.Artifacts]):
  def __init__(self):
    super().__init__(Predicted, gamecorr.GameCorrection())
  
  def pre(self, inp: Predicted) -> gamecorr.Input:
    return gamecorr.Input(ply_boxes=inp.ply_boxes, ocrpreds=inp.ocrpreds, title=inp.title)
  
  def post(self, inp: Predicted, out: gamecorr.Output):
    if out.output.tag == 'correct':
      return Output(
        ocrpreds=inp.ocrpreds, gameId=inp.gameId, model=inp.model,
        imgs=inp.imgs, preprocessed_imgs=inp.preprocessed_imgs, ply_boxes=inp.ply_boxes,
        annotations=out.output.annotations, pgn=out.output.pgn, early=out.output.early, title=inp.title, serving_endpoint=inp.serving_endpoint
      )
    else:
      return Input(gameId=inp.gameId, model=inp.model, imgs=inp.imgs, title=inp.title, serving_endpoint=inp.serving_endpoint)
    
class Pipelines(TypedDict):
  inputval: InputVal
  preprocess: Preprocessing
  predict: Prediction
  correct: Correction

class Queues(TypedDict):
  inputval: Wrapped.Queues
  preprocess: Wrapped.Queues
  predict: Wrapped.Queues
  correct: Wrapped.Queues

@dataclass
class Artifacts:
  api: FastAPI
  processes: Mapping[str, Coroutine]

class Params(GamepreParams):
  tfserving: NotRequired[tfs.Params]
  token: NotRequired[str]

class DFYPipeline(Workflow[Input, Output, Queues, Params, Artifacts, Pipelines]): # type: ignore
  Input = Input
  Output = Output
  Queues = Queues
  Params = Params
  Artifacts = Artifacts
  def __init__(self):
    super().__init__({
      'inputval': InputVal(),
      'preprocess': Preprocessing(),
      'predict': Prediction(),
      'correct': Correction(),
    }, Tin=Input, Tout=Output)

  def run(self, queues: Queues, params: Params):
    logger = params.get('logger') or Logger.click().prefix('[DFY]')
    inpval_api = self.pipelines['inputval'].run(queues['inputval'], InputValidation.Params(logger=logger.prefix('[INPUT VAL]'), images_path=params.get('images_path'), blobs=params['blobs']))
    ocr_coro = self.pipelines['predict'].run(queues['predict'], ocr.Params(logger=logger.prefix('[OCR]'), blobs=params['blobs'], **params.get('tfserving', {})))
    corr_api = self.pipelines['correct'].run(queues['correct'], gamecorr.Params(logger=logger.prefix('[GAME CORRECT]'), images_path=params.get('images_path')))

    gamepre_params = kw.take(GamepreParams, params)
    gamepre_params['logger'] = logger.prefix('[PREPROCESS]')
    gamepre = self.pipelines['preprocess'].run(queues['preprocess'], gamepre_params)

    api = FastAPI()
    api.mount('/inputval', inpval_api)
    api.mount('/preprocess', gamepre.api)
    api.mount('/gamecorr', corr_api)

    images_path = params.get('images_path')
    if images_path is not None:
      from fastapi.staticfiles import StaticFiles
      api.mount('/images', StaticFiles(directory=images_path))

    return Artifacts(
      api=api, processes={
        f'preprocess-{id}': proc
        for id, proc in gamepre.processes.items()
      } | { 'ocr': ocr_coro  }
    )
  