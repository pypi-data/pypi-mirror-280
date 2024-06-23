from typing import Literal
from dataclasses import dataclass
import asyncio
import os
from pydantic import BaseModel
from fastapi import FastAPI, Response, status, Request
from fastapi.staticfiles import StaticFiles
from dslog import Logger
from dslog.uvicorn import setup_loggers_lifespan, DEFAULT_FORMATTER, ACCESS_FORMATTER
from haskellian import iter as I, either as E, Left, Right
from .pipelines import correct as corr, select as sel, validate as val

@dataclass
class CorrectItem(corr.Input):
  id: str
  tag: Literal['correct'] = 'correct'

  @classmethod
  def of(cls, images_path: str):
    def inner(item: tuple[str, corr.Input]) -> CorrectItem:
      id, task = item
      return CorrectItem(img=os.path.join(images_path, task.img), id=id, attempts=task.attempts)
    return inner
  
@dataclass
class SelectItem(sel.Input):
  id: str
  tag: Literal['select'] = 'select'

  @classmethod
  def of(cls, images_path: str):
    def inner(item: tuple[str, sel.Input]) -> SelectItem:
      id, task = item
      return SelectItem(img=os.path.join(images_path, task.img), id=id, model=task.model)
    return inner

@dataclass
class ValidationItem(val.Input):
  id: str
  tag: Literal['validate'] = 'validate'

  @classmethod
  def of(cls, images_path: str):
    def inner(item: tuple[str, val.Input]) -> ValidationItem:
      id, task = item
      return ValidationItem(contoured=os.path.join(images_path, task.contoured), id=id)
    return inner

Item = CorrectItem | SelectItem | ValidationItem
AnnotateResponse = Literal['OK', 'NOT_FOUND', 'BAD_ANNOTATION', 'SERVER_ERROR']

def manual_api(
  *, corr_api: corr.CorrectAPI,
  val_api: val.ValidateAPI,
  sel_api: sel.SelectAPI,
  images_path: str | None = None,
  logger = Logger.rich().prefix('[MANUAL API]')
) -> FastAPI:
  app = FastAPI(
    generate_unique_id_function=lambda route: route.name,
    lifespan=setup_loggers_lifespan(
      access=logger.format(ACCESS_FORMATTER),
      uvicorn=logger.format(DEFAULT_FORMATTER)
    )
  )
  if images_path is not None:
    os.makedirs(images_path, exist_ok=True)
    app.mount('/images', StaticFiles(directory=images_path))

  @app.get('/items')
  async def get_items(r: Request) -> list[Item]:
    base = os.path.join(str(r.base_url), 'images') if images_path is not None else ''
    tasks = (
      corr_api.items().map(lambda e: e | CorrectItem.of(base)).sync(),
      sel_api.items().map(lambda e: e | SelectItem.of(base)).sync(),
      val_api.items().map(lambda e: e | ValidationItem.of(base)).sync(),
    )
    all = I.flatten(await asyncio.gather(*tasks)).sync()
    errs = list(E.filter_lefts(all))
    if errs != []:
      logger('Errors reading tasks:', *errs, level='ERROR')
    return list(E.filter(all))
  
  class CorrectParams(BaseModel):
    corners: corr.Corners
  
  @app.post('/correct')
  async def correct(id: str, params: CorrectParams, r: Response) -> bool:
    x = await corr_api.correct(id, params.corners)
    ok = x.tag == 'right'
    if not ok:
      logger(f'Error correcting item {id}', x.value, level='ERROR')
      r.status_code = status.HTTP_400_BAD_REQUEST
    return ok
  
  class RotateParams(BaseModel):
    rotation: corr.Rotation
  
  @app.post('/rotate')
  async def rotate(id: str, params: RotateParams, r: Response) -> bool:
    x = await corr_api.rotate(id, params.rotation)
    ok = x.tag == 'right'
    if not ok:
      logger(f'Error rotating item {id}', x.value, level='ERROR')
      r.status_code = status.HTTP_400_BAD_REQUEST
    return ok
  
  class SelectParams(BaseModel):
    gridCoords: sel.Rectangle
  
  @app.post('/select')
  async def select(id: str, params: SelectParams, r: Response) -> bool:
    x = await sel_api.select(id, params.gridCoords)
    ok = x.tag == 'right'
    if not ok:
      logger(f'Error selecting item {id}', x.value, level='ERROR')
      r.status_code = status.HTTP_400_BAD_REQUEST
    return ok
  
  @app.post('/recorrect')
  async def recorrect(id: str, r: Response) -> bool:
    x = await sel_api.recorrect(id)
    ok = x.tag == 'right'
    if not ok:
      logger(f'Error recorrecting item {id}', x.value, level='ERROR')
      r.status_code = status.HTTP_400_BAD_REQUEST
    return ok
  
  @app.post('/annotate')
  async def annotate(id: str, annotation: val.Annotation, r: Response) -> AnnotateResponse:
    match await val_api.annotate(id, annotation):
      case Right():
        return 'OK'
      case Left(err):
        if err.reason == 'inexistent-item':
          r.status_code = status.HTTP_404_NOT_FOUND
          return 'NOT_FOUND'
        elif err.reason == 'bad-annotation':
          r.status_code = status.HTTP_400_BAD_REQUEST
          return 'BAD_ANNOTATION'
        else:
          logger(f'Error annotating item {id}', err, level='ERROR')
          r.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
          return 'SERVER_ERROR'
  
  return app