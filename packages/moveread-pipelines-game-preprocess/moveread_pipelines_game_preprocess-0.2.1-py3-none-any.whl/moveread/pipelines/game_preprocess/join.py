from typing import Protocol
import asyncio
from kv.api import KV
from haskellian import either as E
from pipeteer import Task
from dslog import Logger
import moveread.pipelines.preprocess as pre
from ._types import Game, Output

class Artifact(Protocol):
  async def __call__(
    self, *, buffer: KV[dict[str, pre.Output]], games: KV[Game],
    imgGameIds: KV[str], logger: Logger
  ):
    ...

class Join(Task[pre.Output, Output, Artifact]):
  Queues = Task.Queues[pre.Output, Output]
  Artifacts = Artifact

  def __init__(self):
    super().__init__(pre.Output, Output)

  def run(self, queues: Queues) -> Artifact:
    Qin, Qout = queues['Qin'], queues['Qout']
    async def bound(
      *, buffer: KV[dict[str, pre.Output]], games: KV[Game],
      imgGameIds: KV[str], logger: Logger
    ):
      @E.do()
      async def run_one():
        imgId, result = (await Qin.read()).unsafe()
        gameId = (await imgGameIds.read(imgId)).mapl(lambda err: f'Error reading image "{imgId}" gameId: {err}').unsafe()
        logger(f'Received "{imgId}" for "{gameId}"', level='DEBUG')
        game, received = await asyncio.gather(
          games.read(gameId).then(lambda e: e.mapl(lambda err: f'Error reading buffered game: {err}').unsafe()),
          buffer.read(gameId).then(E.get_or({})),
        )

        received_now = dict(received) | { imgId: result }
        receivedIds = set(imgId for imgId, _ in received_now.items())
        requiredIds = set(game.imgIds)
        logger('Received:', receivedIds, 'Required', requiredIds, level='DEBUG')

        if receivedIds == requiredIds:
          next = [received_now[id] for id in game.imgIds]
          (await Qout.push(gameId, next)).unsafe()
          _, e = await asyncio.gather(
            games.delete(gameId).then(E.unsafe),
            buffer.delete(gameId),
          )
          if e.tag == 'left' and e.value.reason != 'inexistent-item':
            e.unsafe()
          logger(f'Joined results for {gameId}')
        else:
          (await buffer.insert(gameId, received_now)).unsafe()
        
        (await imgGameIds.delete(imgId)).unsafe()
        (await Qin.pop(imgId)).unsafe()

      while True:
        r = await run_one()
        if r.tag == 'left':
          logger(r.value, level='ERROR')
          await asyncio.sleep(1)

    return bound
      