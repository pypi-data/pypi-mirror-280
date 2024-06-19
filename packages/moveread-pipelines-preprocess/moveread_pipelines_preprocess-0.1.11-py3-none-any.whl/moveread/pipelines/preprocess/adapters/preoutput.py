from typing import NamedTuple, Callable, Awaitable
import asyncio
import os
from dslog import Logger
from haskellian import either as E, promise as P
from kv.api import KV
import pure_cv as vc
from moveread.annotations.images import ImageMeta
import scoresheet_models as sm
import robust_extraction2 as re
from ..types import Output, ImageResult, Result
from ..spec_codegen import PreoutputPipeline as Preoutput

FetchModel = Callable[[str], Awaitable[re.ExtendedModel]]

def corrected_meta(output: Output) -> ImageMeta:
  match output.tag:
    case 'grid':
      return ImageMeta(grid_coords=output.grid_coords)
    case 'contoured':
      return ImageMeta(box_contours=output.contours)
    
async def extract_boxes(output: Output, img: bytes, *, fetch_model: FetchModel) -> list[bytes]:
  mat = vc.decode(img)
  if output.tag == 'grid':
    model = await fetch_model(output.model)
    boxes = sm.extract_boxes(mat, model, **output.grid_coords)
  else:
    boxes = re.boxes(mat, output.contours) # type: ignore
  return [vc.encode(box, '.jpg') for box in boxes]

class ImageMetas(NamedTuple):
  original: ImageResult
  corrected: ImageResult

def image_metas(output: Output) -> ImageMetas:
  return ImageMetas(
    original=ImageResult(img=output.img, meta=ImageMeta(perspective_corners=output.corners)),
    corrected=ImageResult(img=output.corrected, meta=corrected_meta(output))
  )

async def delete_blobs(output: Output, images: KV[bytes]):
  """Delete all blobs associated to a state"""
  deleted_blobs = [blob for blob in output.blobs if blob != output.img and blob != output.corrected]
  deletions = await asyncio.gather(*[images.delete(blob) for blob in deleted_blobs])
  E.sequence(deletions).unsafe()

async def store_boxes(output: Output, *, images: KV[bytes], fetch_model: FetchModel) -> Result:
  """Extracts boxes and stores results into `ImageMeta`s"""
  original, corrected = image_metas(output)
  img = (await images.read(corrected.img)).unsafe()
  boxes = await extract_boxes(output, img, fetch_model=fetch_model)
  urls = [f'{os.path.splitext(corrected.img)[0]}/boxes/{ply}.jpg' for ply, _ in enumerate(boxes)]
  insertions = await asyncio.gather(*[images.insert(url, box) for url, box in zip(urls, boxes)])
  E.sequence(insertions).unsafe()
  return Result(original=original, corrected=corrected, boxes=urls)

async def postprocess_outputs(output: Preoutput.In, *, images: KV[bytes], fetch_model: FetchModel) -> Preoutput.Out:
  """Store results and delete dangling blobs"""
  result, _ = await asyncio.gather(
    store_boxes(output.root, images=images, fetch_model=fetch_model),
    delete_blobs(output.root, images),
  )
  return result

async def run_preoutput(
  Qin: Preoutput.QueueIn, Qout: Preoutput.QueueOut,
  *, images: KV[bytes],
  logger = Logger.rich().prefix('[PREOUTPUT]')
):
  
  models: dict[str, re.ExtendedModel] = {}
  async def fetch_model(name: str) -> re.ExtendedModel:
    if name not in models:
      logger(f'Fetching model {name}', level='DEBUG')
      models[name] = (await sm.fetch_model(name)).unsafe()
    return models[name]

  @E.do()
  async def run_one():
    id, state = (await Qin.read()).unsafe()
    next = await postprocess_outputs(state, images=images, fetch_model=fetch_model)
    (await Qout.push(id, next)).unsafe()
    (await Qin.pop(id)).unsafe()
  
  while True:
    r = await run_one()
    if r.tag == 'left':
      logger(r.value, level='ERROR')
      await asyncio.sleep(1)