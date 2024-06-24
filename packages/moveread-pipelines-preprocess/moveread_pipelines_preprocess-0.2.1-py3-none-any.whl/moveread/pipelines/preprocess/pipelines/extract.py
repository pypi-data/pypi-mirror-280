from typing_extensions import Any, Coroutine, TypedDict
from dataclasses import dataclass
import asyncio
from uuid import uuid4
from haskellian import funcs as F, either as E, Either
from kv.api import KV
from pipeteer import ReadQueue, WriteQueue, Task
import pure_cv as vc
import robust_extraction2 as re
import scoresheet_models as sm
from dslog import Logger

@dataclass
class Input:
  model: str
  img: str

@dataclass
class Ok:
  contours: list
  corrected: str
  contoured: str

Output = Either[Any, Ok]

@dataclass
class Runner:
  Qin: ReadQueue[Input]
  Qout: WriteQueue[Output]
  logger: Logger
  blobs: KV[bytes]
  models = sm.ModelsCache()

  @E.do()
  async def extract(self, id: str, task: Input): 
    img = (await self.blobs.read(task.img)).unsafe()
    mat = vc.decode(img)
    model = (await self.models.fetch(task.model)).unsafe()
    corr_mat, cnts = re.extract(mat, model).unsafe()
    corrected = vc.encode(corr_mat, format='.jpg')
    contoured = F.pipe(
      vc.draw.contours(corr_mat, cnts, color=(0, 0, 255)), # type: ignore
      vc.descale_h(target_height=768),
      vc.encode(format='.jpg'),
    )
    corr = f'{id}/corrected_{uuid4()}.jpg'
    cont = f'{id}/contoured_{uuid4()}.jpg'
    await asyncio.gather(
      self.blobs.insert(corr, corrected).then(E.unsafe),
      self.blobs.insert(cont, contoured).then(E.unsafe),
    )
    self.logger(f'Inserted corrected image at "{corr}"', level='DEBUG')
    self.logger(f'Inserted contoured image at "{cont}"', level='DEBUG')
    return Ok(contours=cnts.tolist(), corrected=corr, contoured=cont)

  @E.do()
  async def run_one(self):
    id, inp = (await self.Qin.read()).unsafe()
    self.logger(f'Extracting "{id}"')
    res = await self.extract(id, inp)
    (await self.Qout.push(id, res)).unsafe()
    self.logger(f'Extracted "{id}": {"OK" if res.tag == "right" else f"ERR: {res.value}"}')
    (await self.Qin.pop(id)).unsafe()

  async def __call__(self):
    while True:
      e = await self.run_one()
      if e.tag == 'left':
        self.logger(e.value, level='ERROR')
        await asyncio.sleep(1)
      else:
        await asyncio.sleep(0)

class Params(TypedDict):
  blobs: KV[bytes]
  logger: Logger

class Extract(Task[Input, Output, Params, Coroutine]):
  Queues = Task.Queues[Input, Output]
  Params = Params
  Artifacts = Coroutine

  def __init__(self):
    super().__init__(Input, Output)

  def run(self, queues: Queues, params: Params):
    return Runner(**queues, **params)()