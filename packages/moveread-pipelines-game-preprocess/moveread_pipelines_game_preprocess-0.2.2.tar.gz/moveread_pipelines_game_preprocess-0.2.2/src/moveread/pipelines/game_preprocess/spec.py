from typing_extensions import TypedDict, NotRequired
from kv.api import KV
from dslog import Logger
from pipeteer import Workflow
import moveread.pipelines.preprocess as pre
from ._types import Input, Output, Game
from .join import Join
from .preinput import Preinput

class Pipelines(TypedDict):
  preinput: Preinput
  preprocess: pre.Preprocess
  join: Join

class Queues(TypedDict):
  preinput: Preinput.Queues
  preprocess: pre.Preprocess.Queues
  join: Join.Queues

class StorageParams(TypedDict):
  images_path: NotRequired[str | None]
  blobs: KV[bytes]
  buffer: KV[dict[str, pre.Output]]
  games: KV[Game]
  imgGameIds: KV[str]

class Params(StorageParams):
  logger: NotRequired[Logger]

class GamePreprocess(Workflow[Input, Output, Queues, Params, pre.Artifacts, Pipelines]): # type: ignore
  Input = Input
  Output = Output
  Queues = Queues
  Params = Params
  Artifacts = pre.Artifacts

  def __init__(self):
    super().__init__({
      'preinput': Preinput(),
      'preprocess': pre.Preprocess(),
      'join': Join(),
    })

  def run(self, queues: Queues, params: Params):

    logger = params.get('logger') or Logger.click(); blobs = params['blobs']; images_path = params.get('images_path')
    buffer = params['buffer']; games = params['games']; imgGameIds = params['imgGameIds']

    artifs = self.pipelines['preprocess'].run(queues['preprocess'], pre.Params(logger=logger, blobs=blobs, images_path=images_path))
    artifs.processes = {
      f'preprocess-{k}': v for k, v in artifs.processes.items()
    } | {
      'preinput': self.pipelines['preinput'].run(queues['preinput'], Preinput.Params(logger=logger, games=games, imgGameIds=imgGameIds)),
      'join': self.pipelines['join'].run(queues['join'], Join.Params(logger=logger, buffer=buffer, games=games, imgGameIds=imgGameIds)),
    }
    return artifs