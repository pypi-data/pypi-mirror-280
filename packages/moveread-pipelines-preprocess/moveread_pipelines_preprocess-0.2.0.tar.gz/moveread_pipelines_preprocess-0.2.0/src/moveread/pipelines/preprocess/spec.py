from typing import TypedDict, Any, Coroutine, Callable, Mapping, Protocol
from dataclasses import dataclass
from pipeteer import Wrapped, Workflow, Task
from fastapi import FastAPI
from dslog import Logger
from kv.api import KV
from ._types import BaseInput, Corrected, Extracted, Selected, Output
from .pipelines import correct as corr, extract as extr, select as sel, validate as val, preoutput
from .api import manual_api

@dataclass
class Extract:
  input: BaseInput | Corrected
  def pre(self) -> extr.Input:
    return extr.Input(model=self.input.model, img=self.input.img)
  def post(self, out: extr.Output) -> 'State':
    inp = self.input
    if out.tag == 'left':
      if isinstance(inp, Corrected):
        return Select(model=inp.model, img=inp.img, corrected=inp.corrected, attempts=inp.attempts+1)
      else:
        return Correct(model=inp.model, img=inp.img, attempts=inp.attempts+1)
    else:
      o = out.value
      return Validate(model=inp.model, img=inp.img, corrected=o.corrected, contours=o.contours, contoured=o.contoured, attempts=inp.attempts+1)
    
  @staticmethod
  def new(img: str, model: str):
    return Extract(input=BaseInput(model=model, img=img, attempts=0))


class Correct(BaseInput):
  def pre(self) -> corr.Input:
    return corr.Input(img=self.img, attempts=self.attempts)
  def post(self, out: corr.Output) -> 'State':
    if out.tag == 'corrected':
      if out.next == 'reextract':
        c = Corrected(model=self.model, img=self.img, corrected=out.corrected, attempts=self.attempts)
        return Extract(input=c)
      else:
        return Select(model=self.model, img=self.img, corrected=out.corrected, attempts=self.attempts)
    else:
      return Extract(input=BaseInput(model=self.model, img=out.rotated, attempts=self.attempts))

class Validate(Extracted):
  def pre(self) -> val.Input:
    return val.Input(contoured=self.contoured)
  def post(self, out: val.Annotation) -> 'State':
    if out == 'correct':
      extr = Extracted(model=self.model, img=self.img, corrected=self.corrected, contours=self.contours, contoured=self.contoured, attempts=self.attempts)
      return Preoutput(result=extr)
    elif out == 'perspective-correct':
      return Select(model=self.model, img=self.img, corrected=self.corrected, attempts=self.attempts)
    elif out == 'incorrect':
      return Correct(model=self.model, img=self.img, attempts=self.attempts)
    else:
      raise ValueError(f'Unexpected annotation for validate output: {out}')

class Select(Corrected):
  def pre(self) -> sel.Input:
    return sel.Input(model=self.model, img=self.corrected)
  def post(self, out: sel.Output) -> 'State':
    if out.tag == 'selected':
      sel = Selected(model=self.model, img=self.img, corrected=self.corrected, grid_coords=out.grid_coords, attempts=self.attempts)
      return Preoutput(result=sel)
    elif out.tag == 'recorrect':
      return Correct(model=self.model, img=self.img, attempts=self.attempts)
    else:
      raise ValueError(f'Unexpected tag for select output: {out.tag}')

@dataclass
class Preoutput:
  result: Selected | Extracted
  def pre(self) -> preoutput.Input:
    return preoutput.Input(result=self.result)
  def post(self, out: Output) -> 'State':
    return out

State = Extract | Correct | Validate | Select | Preoutput | Output
Input = Extract

class Queues(TypedDict):
  extract: Wrapped.Queues
  correct: Wrapped.Queues
  validate: Wrapped.Queues
  select: Wrapped.Queues
  preoutput: Wrapped.Queues

class Pipelines(TypedDict): 
  extract: Wrapped[Extract, Any, extr.Input, Any, Task.Queues, extr.Artifact]
  correct: Wrapped[Correct, Any, corr.Input, Any, Task.Queues, corr.Artifact]
  validate: Wrapped[Validate, Any, val.Input, Any, Task.Queues, val.ValidateAPI]
  select: Wrapped[Select, Any, sel.Input, Any, Task.Queues, sel.SelectAPI]
  preoutput: Wrapped[Preoutput, Any, preoutput.Input, Any, Task.Queues, preoutput.Artifact]

@dataclass
class Artifacts:
  api: FastAPI
  processes: dict[str, Coroutine]

class Artifact(Protocol):
  def __call__(self, *, logger: Logger, blobs: KV[bytes], images_path: str | None = None) -> Artifacts:
    ...

class Preprocess(Workflow[Input, Any, Pipelines, Queues, Artifact]): # type: ignore
  Queues = Queues
  Artifacts = Artifacts
  def __init__(self):
    super().__init__({
      'extract': Wrapped.of(Extract, extr.Extract(), Extract.pre, Extract.post),
      'correct': Wrapped.of(Correct, corr.Correct(), Correct.pre, Correct.post),
      'validate': Wrapped.of(Validate, val.Validate(), Validate.pre, Validate.post),
      'select': Wrapped.of(Select, sel.Select(), Select.pre, Select.post),
      'preoutput': Wrapped.of(Preoutput, preoutput.Preoutput(), Preoutput.pre, Preoutput.post),
    })

  def run(self, queues: Queues) -> Artifact:
    def bound(*, logger: Logger, blobs: KV[bytes], images_path: str | None = None):
      api = manual_api(
        corr_api=self.pipelines['correct'].run(queues['correct'])(blobs=blobs, logger=logger.prefix('[CORRECT]')),
        val_api=self.pipelines['validate'].run(queues['validate']),
        sel_api=self.pipelines['select'].run(queues['select']),
        images_path=images_path, logger=logger.prefix('[API]')
      )
      procs = {
        'extract': self.pipelines['extract'].run(queues['extract'])(blobs=blobs, logger=logger.prefix('[EXTRACT]')),
        'preoutput': self.pipelines['preoutput'].run(queues['preoutput'])(blobs=blobs, logger=logger.prefix('[PREOUTPUT]')),
      }
      return Artifacts(api=api, processes=procs)

    return bound
  