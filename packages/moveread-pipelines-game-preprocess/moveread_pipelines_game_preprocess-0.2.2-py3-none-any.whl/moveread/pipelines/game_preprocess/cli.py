from argparse import ArgumentParser

def main():
  parser = ArgumentParser()
  parser.add_argument('-d', '--db-path', required=True)
  parser.add_argument('--images', required=True)

  parser.add_argument('-p', '--port', default=8000, type=int)
  parser.add_argument('--host', default='0.0.0.0', type=str)

  args = parser.parse_args()


  import os
  from dslog import Logger
  db_path = os.path.join(os.getcwd(), args.db_path)
  images_path = os.path.join(os.getcwd(), args.images)
  
  logger = Logger.click().prefix('[GAME PREPROCESS]')
  logger(f'Running preprocessing...')
  logger(f'Images path: "{images_path}"')
  logger(f'DB path: "{db_path}"')
  
  import asyncio
  from multiprocessing import Process
  from kv.fs import FilesystemKV
  from kv.sqlite import SQLiteKV
  from pipeteer import QueueKV
  import uvicorn
  from fastapi.middleware.cors import CORSMiddleware
  import moveread.pipelines.preprocess as pre
  from moveread.pipelines.game_preprocess import GamePreprocess, Output, Game

  images = FilesystemKV[bytes](images_path)

  def get_queue(path, type: type):
    return QueueKV.sqlite(type, db_path, table='-'.join(['queues', *path]))
  
  Qout = get_queue(('output',), Output)
  wkf = GamePreprocess()
  params = GamePreprocess.Params(
    logger=logger, blobs=images, images_path=images_path,
    buffer=SQLiteKV.validated(dict[str, pre.Output], db_path, 'buffer'),
    games=SQLiteKV.validated(Game, db_path, 'games'),
    imgGameIds=SQLiteKV.at(db_path, 'game-ids')
  )
  Qs = wkf.connect(Qout, get_queue, params)
  artifs = wkf.run(Qs, params)
  artifs.api.add_middleware(CORSMiddleware, allow_origins=['*'], allow_credentials=True, allow_methods=['*'], allow_headers=['*'])

  ps = {
    id: Process(target=asyncio.run, args=(f,)) for id, f in artifs.processes.items()
  } | {
    'api': Process(target=uvicorn.run, args=(artifs.api,), kwargs={'host': args.host, 'port': args.port})
  }
  for id, p in ps.items():
    p.start()
    logger(f'Process "{id}" started at PID {p.pid}')
  for p in ps.values():
    p.join()
  

if __name__ == '__main__':
  import sys
  import os
  os.chdir('/home/m4rs/mr-github/rnd/data/moveread-pipelines/backend/3.game-preprocess/')
  sys.argv.extend('-q demo/queues.sqlite --images demo/images/'.split(' '))
  main()