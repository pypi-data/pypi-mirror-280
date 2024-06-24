from argparse import ArgumentParser

def main():
  parser = ArgumentParser()
  parser.add_argument('-q', '--queues', required=True, help='Queues DB path')
  parser.add_argument('--images', required=True)

  parser.add_argument('-p', '--port', default=8000, type=int)
  parser.add_argument('--host', default='0.0.0.0', type=str)

  args = parser.parse_args()


  import os
  from dslog import Logger
  queues_path = os.path.join(os.getcwd(), args.queues)
  images_path = os.path.join(os.getcwd(), args.images)
  
  logger = Logger.click().prefix('[INPUT VAL]')
  logger(f'Running input validation...')
  logger(f'Images path: "{images_path}"')
  logger(f'Queues path: "{queues_path}"')
  
  import uvicorn
  from fastapi.middleware.cors import CORSMiddleware
  from pipeteer import QueueKV
  from moveread.pipelines.input_validation import InputValidation, Output
  from dslog import Logger
  from kv.fs import FilesystemKV

  def get_queue(path, type: type):
    return QueueKV.sqlite(type, queues_path, '-'.join(path))

  Qout = get_queue(('output',), Output)
  pipeline = InputValidation()
  blobs = FilesystemKV[bytes](images_path)
  params = InputValidation.Params(logger=Logger.click().prefix('[INPUT VAL]'), images_path=images_path, blobs=blobs)
  Qs = pipeline.connect(Qout, get_queue, params)
  api = pipeline.run(Qs, params)
  api.add_middleware(CORSMiddleware, allow_origins=['*'], allow_methods=['*'], allow_headers=['*'])
  uvicorn.run(api, port=args.port, host=args.host)

if __name__ == '__main__':
  import sys
  import os
  os.chdir('/home/m4rs/mr-github/rnd/data/moveread-pipelines/backend/input-validation/demo')
  sys.argv.extend('-q queues.sqlite --images images'.split(' '))
  main()