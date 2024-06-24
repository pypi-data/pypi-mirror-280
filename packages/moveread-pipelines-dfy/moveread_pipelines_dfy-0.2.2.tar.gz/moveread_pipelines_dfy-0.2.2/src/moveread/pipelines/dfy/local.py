from typing import Sequence, TypeVar
import os
from pipeteer import QueueKV
from kv.fs import FilesystemKV
from kv.sqlite import SQLiteKV
import moveread.pipelines.preprocess as pre
from moveread.pipelines.game_preprocess import StorageParams, Game

T = TypeVar('T')

def queue_factory(db_path: str):
  def get_queue(path: Sequence[str|int], type: type[T]) -> QueueKV[T]:
    return QueueKV.sqlite(type, db_path, '-'.join(str(p) for p in (path or ['Qin'])))
  return get_queue

def local_storage(
  base_path: str, *,
  db_relpath: str = 'data.sqlite',
  images_relpath: str = 'images',
) -> StorageParams:
  """Scaffold local storage for the DFY pipeline."""

  db_path = os.path.join(base_path, db_relpath)
  images_path = os.path.join(base_path, images_relpath)
  return StorageParams(
    blobs=FilesystemKV[bytes](images_path),
    games=SQLiteKV.validated(Game, db_path, 'games'),
    imgGameIds=SQLiteKV[str].at(db_path, 'game-ids'),
    buffer=SQLiteKV.validated(dict[str, pre.Output], db_path, 'received-imgs'),
    images_path=images_path,
  )