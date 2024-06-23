from typing import TypedDict, Protocol, NotRequired, Unpack
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

class Params(TypedDict):
  images_path: NotRequired[str | None]
  blobs: KV[bytes]
  buffer: KV[dict[str, pre.Output]]
  games: KV[Game]
  imgGameIds: KV[str]

class ArtifactsProto(Protocol):
  def __call__(self, *, logger: Logger, **params: Unpack[Params]) -> pre.Preprocess.Artifacts:
    ...

class GamePreprocess(Workflow[Input, Output, Pipelines, Queues, ArtifactsProto]): # type: ignore
  Input = Input
  Output = Output
  Queues = Queues
  Artifacts = ArtifactsProto

  def __init__(self):
    super().__init__({
      'preinput': Preinput(),
      'preprocess': pre.Preprocess(),
      'join': Join(),
    })

  def run(self, queues: Queues) -> ArtifactsProto:
    def bound(
      *, logger: Logger, blobs: KV[bytes], images_path: str | None = None,
      buffer: KV[dict[str, pre.Output]], games: KV[Game], imgGameIds: KV[str],
    ):
      artifs = self.pipelines['preprocess'].run(queues['preprocess'])(logger=logger, blobs=blobs, images_path=images_path)
      artifs.processes = {
        f'preprocess-{k}': v for k, v in artifs.processes.items()
      } | {
        'preinput': self.pipelines['preinput'].run(queues['preinput'])(logger=logger, games=games, imgGameIds=imgGameIds),
        'join': self.pipelines['join'].run(queues['join'])(logger=logger, buffer=buffer, games=games, imgGameIds=imgGameIds),
      }
      return artifs
    
    return bound