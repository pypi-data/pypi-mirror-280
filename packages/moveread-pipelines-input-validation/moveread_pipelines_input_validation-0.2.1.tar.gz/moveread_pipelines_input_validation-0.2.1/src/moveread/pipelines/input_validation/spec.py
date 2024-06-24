from typing_extensions import TypedDict, NotRequired
from functools import partial
import asyncio
from haskellian import either as E, funcs as F
from pipeteer import GetQueue, Task, WriteQueue
from kv.api import KV
from fastapi import FastAPI
from dslog import Logger
import pure_cv as vc
from ._types import Input, Output
from .api import fastapi, InputValidationSDK

class Params(TypedDict):
  blobs: KV
  logger: Logger
  images_path: NotRequired[str | None]
  descale_height: NotRequired[int]

def descaled_path(img: str):
  name, _ = img.split('.')
  return f'{name}_rescaled.jpg'

def unrescale_path(img: str):
  name, ext = img.split('.')
  return name.removesuffix('_rescaled') + '.' + ext

def descale_img(img: bytes, descale_height: int):
  return F.pipe(img, vc.decode, vc.descale_h(target_height=descale_height), vc.encode(format='.jpg'))

@E.do()
async def pre(input: Input, *, blobs: KV[bytes], descale_height: int) -> Input:
  """Descale the images and pass them as inputs"""
  tasks = [blobs.read(img) for img in input.imgs]
  imgs = E.sequence(await asyncio.gather(*tasks)).unsafe()

  rescaled_urls = [descaled_path(img) for img in input.imgs]
  descaled_imgs = [descale_img(img, descale_height) for img in imgs]
  tasks = [blobs.insert(url, img) for url, img in zip(rescaled_urls, descaled_imgs)]
  E.sequence(await asyncio.gather(*tasks)).unsafe()
  return Input(gameId=input.gameId, imgs=rescaled_urls)
  
def post(output: Output) -> Output:
  """Adjust the output URLs to the original images"""
  return Output(gameId=output.gameId, imgs=[unrescale_path(img) for img in output.imgs])

class InputValidation(Task[Input, Output, Params, FastAPI]):
  Input = Input
  Output = Output
  Queues = Task.Queues[Input, Output]
  Params = Params
  Artifacts = FastAPI

  def __init__(self):
    super().__init__(Input, Output)

  def push_queue(self, get_queue: GetQueue, params: Params, /, *, prefix: tuple[str | int, ...] = ()) -> WriteQueue[Input]:
    return get_queue(prefix, self.Tin).safe_apremap(partial(pre, blobs=params['blobs'], descale_height=params.get('descale_height', 1024)))

  def run(self, queues: Queues, params: Params) -> FastAPI:
    Qin, Qout = queues['Qin'], queues['Qout']
    sdk = InputValidationSDK(Qin, Qout.premap(post))
    return fastapi(sdk, logger=params['logger'], images_path=params.get('images_path'))