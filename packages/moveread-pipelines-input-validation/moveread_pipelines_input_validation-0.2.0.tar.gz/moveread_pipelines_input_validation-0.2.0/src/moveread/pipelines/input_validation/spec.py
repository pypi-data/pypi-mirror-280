from typing import Protocol
from pipeteer import Task
from fastapi import FastAPI
from dslog import Logger
from ._types import Input, Output
from .api import fastapi, InputValidationSDK

class Artifact(Protocol):
  def __call__(self, *, logger: Logger, images_path: str | None = None) -> FastAPI:
    ...

class InputValidation(Task[Input, Output, Artifact]):
  Input = Input
  Output = Output
  Queues = Task.Queues[Input, Output]
  Artifacts = Artifact

  def __init__(self):
    super().__init__(Input, Output)

  def run(self, queues: Queues) -> Artifact:
    def bound(*, logger: Logger, images_path: str | None = None):
      sdk = InputValidationSDK(**queues)
      return fastapi(sdk, logger=logger, images_path=images_path)
    return bound