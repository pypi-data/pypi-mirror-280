from argparse import ArgumentParser

def main():
  parser = ArgumentParser()
  parser.add_argument('-i', '--images', required=True, type=str)
  parser.add_argument('-q', '--queues', required=True, type=str)

  parser.add_argument('-p', '--port', default=8000, type=int)
  parser.add_argument('--host', default='0.0.0.0', type=str)

  args = parser.parse_args()

  import os
  from dslog import Logger

  images = os.path.join(os.getcwd(), args.images)
  db_path = os.path.join(os.getcwd(), args.queues)

  logger = Logger.click().prefix('[GAME CORRECTION]')
  logger(f'Running API...')
  logger(f'- Queues path: "{db_path}"')
  logger(f'- Images path: "{images}"')
  os.makedirs(images, exist_ok=True)

  from fastapi.middleware.cors import CORSMiddleware
  import uvicorn
  from pipeteer import QueueKV
  from moveread.pipelines.game_correction import GameCorrection, Output

  def get_queue(path, type):
    return QueueKV.sqlite(type, db_path, '-'.join(path))

  Qout = get_queue(('output',), Output)
  pipe = GameCorrection()
  params = GameCorrection.Params(images_path=images, logger=logger)
  Qs = pipe.connect(Qout, get_queue, params)
  api = pipe.run(Qs, params)
  api.add_middleware(CORSMiddleware, allow_origins=['*'], allow_methods=['*'], allow_headers=['*'])
  uvicorn.run(api, port=args.port, host=args.host)
  
if __name__ == '__main__':
  import sys
  sys.argv.extend('-p 8001 -i demo/images -q demo/queues.sqlite'.split(' '))
  main()