from typing import Literal
from dataclasses import dataclass
from moveread.boxes import Rectangle
from moveread.annotations import ImageMeta

@dataclass
class ImgOutput:
  img: str
  meta: ImageMeta | None = None

@dataclass
class Output:
  original: ImgOutput
  corrected: ImgOutput
  boxes: list[str]

@dataclass
class BaseInput:
  img: str
  model: str
  attempts: int

@dataclass
class Corrected(BaseInput):
  corrected: str

@dataclass
class Extracted(Corrected):
  contours: list
  contoured: str
  tag: Literal['extracted'] = 'extracted'

@dataclass
class Selected(Corrected):
  grid_coords: Rectangle
  tag: Literal['selected'] = 'selected'