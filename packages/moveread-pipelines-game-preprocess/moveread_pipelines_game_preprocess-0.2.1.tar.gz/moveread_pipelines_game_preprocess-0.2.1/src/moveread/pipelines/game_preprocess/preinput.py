from typing import Protocol
import asyncio
from kv.api import KV
from haskellian import either as E
from pipeteer import Task
from dslog import Logger
import moveread.pipelines.preprocess as pre
from ._types import Input, Game

class Artifact(Protocol):
  async def __call__(self, *, games: KV[Game], imgGameIds: KV[str], logger: Logger):
    ...

class Preinput(Task[Input, pre.Input, Artifact]):
  Queues = Task.Queues[Input, pre.Input]
  Artifacts = Artifact

  def __init__(self):
    super().__init__(Input, pre.Input)

  def run(self, queues: Queues) -> Artifact:
    Qin, Qout = queues['Qin'], queues['Qout']
    async def bound(*, games: KV[Game], imgGameIds: KV[str], logger: Logger):
      @E.do()
      async def input_one():
        gameId, task = (await Qin.read()).unsafe()
        imgIds = [f'{gameId}-{i}' for i in range(len(task.imgs))]
        (await games.insert(gameId, Game(model=task.model, imgIds=imgIds))).unsafe()
        E.sequence(await asyncio.gather(*[
          imgGameIds.insert(imgId, gameId)
          for imgId in imgIds
        ])).unsafe()
        E.sequence(await asyncio.gather(*[
          Qout.push(imgId, pre.Input.new(model=task.model, img=img))
          for imgId, img in zip(imgIds, task.imgs)
        ])).unsafe()
        (await Qin.pop(gameId)).unsafe()
        logger(f'Pushed tasks from "{gameId}"', level='DEBUG')

      while True:
        r = await input_one()
        if r.tag == 'left':
          logger(r.value, level='ERROR')
          await asyncio.sleep(1)

    return bound