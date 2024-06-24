from typing_extensions import Coroutine, TypedDict
from dataclasses import dataclass
import asyncio
import os
from haskellian import either as E
from kv.api import KV
from pipeteer import ReadQueue, WriteQueue, Task
from dslog import Logger
import pure_cv as vc
import scoresheet_models as sm
import robust_extraction2 as re
from moveread.annotations.images import ImageMeta
from .._types import Selected, Extracted, Output, ImgOutput

@dataclass
class Input:
  result: Selected | Extracted

def corrected_meta(output: Selected | Extracted) -> ImageMeta:
  match output.tag:
    case 'selected':
      return ImageMeta(grid_coords=output.grid_coords)
    case 'extracted':
      return ImageMeta(box_contours=output.contours)
    
def image_metas(output: Selected | Extracted):
  original = ImgOutput(img=output.img)
  corrected = ImgOutput(img=output.corrected, meta=corrected_meta(output))
  return original, corrected

@dataclass
class Runner:
  Qin: ReadQueue[Input]
  Qout: WriteQueue[Output]
  blobs: KV[bytes]
  logger: Logger
  models = sm.ModelsCache()
    
  @E.do()
  async def extract_boxes(self, output: Selected | Extracted, img: bytes) -> list[bytes]:
    mat = vc.decode(img)
    if output.tag == 'selected':
      model = (await self.models.fetch(output.model)).unsafe()
      boxes = sm.extract_boxes(mat, model, **output.grid_coords)
    else:
      boxes = re.boxes(mat, output.contours) # type: ignore
    return [vc.encode(box, '.jpg') for box in boxes]
  
  @E.do()
  async def store_boxes(self, output: Selected | Extracted) -> Output:
    """Extracts boxes and stores results into `ImageMeta`s"""
    original, corrected = image_metas(output)
    img = (await self.blobs.read(corrected.img)).unsafe()
    boxes = (await self.extract_boxes(output, img)).unsafe()
    urls = [f'{os.path.splitext(corrected.img)[0]}/boxes/{ply}.jpg' for ply, _ in enumerate(boxes)]
    insertions = await asyncio.gather(*[self.blobs.insert(url, box) for url, box in zip(urls, boxes)])
    E.sequence(insertions).unsafe()
    self.logger(f'Inserted {len(boxes)} boxes: {", ".join(urls[:2])}, ...', level='DEBUG')
    return Output(original=original, corrected=corrected, boxes=urls)

  @E.do()
  async def delete_blobs(self, id: str, output: Extracted | Selected):
    keys = (await self.blobs.keys()).unsafe()
    def delete(blob: str) -> bool:
      return blob.startswith(id) and blob != output.img and blob != output.corrected and not 'boxes' in blob
    delete_blobs = list(filter(delete, keys))
    deletions = await asyncio.gather(*[self.blobs.delete(blob) for blob in delete_blobs])
    E.sequence(deletions).unsafe()
    self.logger(f'Deleted {len(delete_blobs)} blobs: {delete_blobs}', level='DEBUG')
    

  @E.do()
  async def run_one(self):
    id, inp = (await self.Qin.read()).unsafe()
    next = (await self.store_boxes(inp.result)).unsafe()
    (await self.delete_blobs(id, inp.result)).unsafe()
    (await self.Qout.push(id, next)).unsafe()
    (await self.Qin.pop(id)).unsafe()
    self.logger(f'Outputted "{id}')

  async def __call__(self):
    while True:
      r = await self.run_one()
      if r.tag == 'left':
        self.logger(r.value, level='ERROR')
        await asyncio.sleep(1)

class Params(TypedDict):
  logger: Logger
  blobs: KV[bytes]

class Preoutput(Task[Input, Output, Params, Coroutine]):
  Queues = Task.Queues[Input, Output]
  Params = Params
  Artifacts = Coroutine

  def __init__(self):
    super().__init__(Input, Output)

  def run(self, queues: Task.Queues[Input, Output], params: Params):
    return Runner(**queues, **params)()
