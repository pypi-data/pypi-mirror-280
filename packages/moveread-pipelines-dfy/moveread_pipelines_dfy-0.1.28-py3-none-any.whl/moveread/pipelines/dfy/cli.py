from argparse import ArgumentParser
import os

def env(variable: str, *, default = None, required: bool = True) -> dict:
  if (value := os.getenv(variable, default)) is not None:
    return dict(default=value)
  return dict(required=required)

def main():
  parser = ArgumentParser()
  parser.add_argument('-b', '--base-path', required=True)
  parser.add_argument('--token', **env('TOKEN', default='secret'), type=str)

  parser.add_argument('--tfs-host', **env('TFS_HOST', required=False), type=str)
  parser.add_argument('--tfs-port', **env('TFS_PORT', required=False), type=str)
  parser.add_argument('--tfs-endpoint', **env('TFS_ENDPOINT', default='/v1/models/baseline:predict'), type=str)

  parser.add_argument('-p', '--port', default=8000, type=int)
  parser.add_argument('--host', default='0.0.0.0', type=str)
  parser.add_argument('--cors', default=['*'], nargs='*', type=str, help='CORS allowed origins')

  args = parser.parse_args()

  import os
  from dslog import Logger
  base_path = os.path.join(os.getcwd(), args.base_path)
  
  logger = Logger.click().prefix('[DFY]')
  logger(f'Running DFY pipeline at "{base_path}"...')
  
  import asyncio
  from multiprocessing import Process
  import uvicorn
  from pydantic import BaseModel
  from fastapi import Request, Response
  from fastapi.middleware.cors import CORSMiddleware
  from moveread.pipelines.dfy import Workflow, local_storage, local_queues, Input, Result
  import tf.serving as tfs
  from q.http.server import read_api, write_api
  import kv.rest
  from dslog import Logger
  from pipeteer import flatten_queues

  tfparams = tfs.Params(host=args.tfs_host, port=args.tfs_port, endpoint=args.tfs_endpoint)
  tfparams: tfs.Params = { k: v for k, v in tfparams.items() if v is not None } # type: ignore

  logger = Logger.click().prefix('[DFY]')

  queues, Qout = local_queues(base_path)
  storage = local_storage(base_path)
  artifacts = Workflow.artifacts(**queues['internal'])(
    tfserving=tfparams, logger=logger,
    token=args.token, **storage
  )
  artifacts.api.mount('/input/write', write_api(queues['Qin'], Type=Input))
  artifacts.api.mount('/output/read', read_api(Qout, Type=Result))
  artifacts.api.mount('/blobs', kv.rest.api(storage['images']))

  @artifacts.api.get('/clean')
  def clean():
    from shutil import rmtree
    rmtree(base_path, ignore_errors=True)
    local_queues(base_path)
    local_storage(base_path)

  for path, q in flatten_queues(queues['internal']): # type: ignore
    endpoint = '/queues/' + '/'.join(path) + '/read'
    artifacts.api.mount(endpoint, read_api(q, dump=BaseModel.model_dump_json))

  artifacts.api.add_middleware(
    CORSMiddleware,
    allow_origins=args.cors,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
  )

  @artifacts.api.middleware('http')
  async def auth_middleware(request: Request, call_next):
    images_path = request.url.path.startswith('/images/') and not '..' in request.url.path # could that hack work? let's just be safe
    if request.url.path == '/gamecorr/preds' or images_path or request.method == 'OPTIONS':
      return await call_next(request)
  
    auth = request.headers.get('Authorization')
    if not auth or len(parts := auth.split(' ')) != 2 or parts[0] != 'Bearer':
      logger(f'Bad authorization:', auth, level='DEBUG')
      return Response(status_code=401)
    if parts[1] != args.token:
      logger(f'Bad token: "{parts[1]}"', level='DEBUG')
      return Response(status_code=401)
    
    return await call_next(request)

  ps = {
    id: Process(target=asyncio.run, args=(f,))
    for id, f in artifacts.processes.items()
  } | {
    'api': Process(target=uvicorn.run, args=(artifacts.api,), kwargs={'host': args.host, 'port': args.port})
  }
  for id, p in ps.items():
    p.start()
    logger(f'Process "{id}" started at PID {p.pid}')
  for p in ps.values():
    p.join()

if __name__ == '__main__':
  import sys
  import os
  path = '/home/m4rs/mr-github/rnd/data/moveread-pipelines/infra/data'
  os.makedirs(path, exist_ok=True)
  os.chdir(path)
  sys.argv.extend('-b .'.split(' '))
  main()