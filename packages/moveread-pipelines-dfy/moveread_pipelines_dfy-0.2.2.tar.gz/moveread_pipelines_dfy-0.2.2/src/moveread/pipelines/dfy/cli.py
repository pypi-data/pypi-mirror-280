from argparse import ArgumentParser
import os

def env(variable: str, *, default = None, required: bool = True) -> dict:
  if (value := os.getenv(variable, default)) is not None:
    return dict(default=value)
  return dict(required=required)

def main():
  parser = ArgumentParser()
  parser.add_argument('-b', '--base-path', required=True)
  parser.add_argument('-l', '--logs', required=True, help='Path to logs directory')
  parser.add_argument('--logpipe', required=False, help='Output log file path')
  parser.add_argument('--token', **env('TOKEN', default='secret'), type=str)

  parser.add_argument('--tfs-host', **env('TFS_HOST', required=False), type=str)
  parser.add_argument('--tfs-port', **env('TFS_PORT', required=False), type=str)
  parser.add_argument('--tfs-endpoint', **env('TFS_ENDPOINT', default='/v1/models/baseline:predict'), type=str)

  parser.add_argument('-p', '--port', default=8000, type=int)
  parser.add_argument('--host', default='0.0.0.0', type=str)
  parser.add_argument('--cors', default=['*'], nargs='*', type=str, help='CORS allowed origins')

  args = parser.parse_args()

  import os
  from dslog import loggers, formatters, Logger
  base_path = os.path.join(os.getcwd(), args.base_path)
  
  if args.logpipe:
    logger = loggers.file(args.logpipe).format(formatters.click).prefix('[DFY]')
  else:
    logger = Logger.click().prefix('[DFY]')
  logger(f'Running DFY pipeline at "{base_path}"...')

  import asyncio
  from multiprocessing import Process
  import uvicorn
  from fastapi import Request, Response
  from fastapi.middleware.cors import CORSMiddleware
  import tf.serving as tfs
  from moveread.pipelines.dfy import DFYPipeline, queue_factory, Output, local_storage
  from pipeteer import http
  from kv.fs import FilesystemKV
  import kv.rest

  tfparams = tfs.Params(host=args.tfs_host, port=args.tfs_port, endpoint=args.tfs_endpoint)
  tfparams: tfs.Params = { k: v for k, v in tfparams.items() if v is not None } # type: ignore

  pipe = DFYPipeline()
  get_queue = queue_factory(os.path.join(base_path, 'queues.sqlite'))
  Qout = get_queue(('output',), Output)
  storage = local_storage(base_path)
  params = DFYPipeline.Params(logger=logger, token=args.token, tfserving=tfparams, **storage)
  Qs = pipe.connect(Qout, get_queue, params)
  
  artifs = pipe.run(Qs, params)

  artifs.api.mount('/queues', http.mount(pipe, Qout, get_queue, params))
  artifs.api.mount('/blobs', kv.rest.api(storage['blobs']))
  artifs.api.mount('/logs', kv.rest.api(FilesystemKV(args.logs)))

  artifs.api.add_middleware(CORSMiddleware, allow_origins=args.cors, allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

  @artifs.api.middleware('http')
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
    for id, f in artifs.processes.items()
  } | {
    'api': Process(target=uvicorn.run, args=(artifs.api,), kwargs={'host': args.host, 'port': args.port})
  }
  for id, p in ps.items():
    p.start()
    logger(f'Process "{id}" started at PID {p.pid}')
  for p in ps.values():
    p.join()

if __name__ == '__main__':
  import os
  import sys
  os.chdir('/home/m4rs/mr-github/modes/dfy/dfy-pipeline/dfy/dev')
  args = '-b demo --port 8324 --logs demo/logs'
  sys.argv.extend(args.split(' '))
  main()