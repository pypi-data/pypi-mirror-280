from typing import Literal
from dataclasses import dataclass
from haskellian import Left, either as E
from pipeteer import ReadQueue, WriteQueue, Task

@dataclass
class Input:
  contoured: str

Annotation = Literal['incorrect', 'correct', 'perspective-correct']

@dataclass
class ValidateAPI:

  Qin: ReadQueue[Input]
  Qout: WriteQueue[Annotation]

  def items(self):
    return self.Qin.items()
  
  @E.do()
  async def annotate(self, id: str, annotation: Annotation):
    (await self.Qin.read(id)).unsafe()
    (await self.Qout.push(id, annotation)).unsafe() # type: ignore
    (await self.Qin.pop(id)).unsafe()

class Validate(Task[Input, Annotation, ValidateAPI]):

  Queues = Task.Queues[Input, Annotation]
  Artifacts = ValidateAPI

  def __init__(self):
    super().__init__(Input, Annotation)

  def run(self, queues: Task.Queues[Input, Annotation]) -> ValidateAPI:
    return ValidateAPI(**queues)
  
