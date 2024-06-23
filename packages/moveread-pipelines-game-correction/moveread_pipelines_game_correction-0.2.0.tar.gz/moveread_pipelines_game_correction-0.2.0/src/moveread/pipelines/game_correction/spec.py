from typing import Protocol
from functools import partial
from pipeteer import Task
from dslog import Logger
from fastapi import FastAPI
from ._types import Input, Output
from .api import fastapi
from .sdk import CorrectionSDK

class Artifact(Protocol):
  def __call__(self, *, images_path: str | None = None, logger: Logger = Logger.empty()) -> FastAPI:
    ...

class GameCorrection(Task[Input, Output, Artifact]):
  Queues = Task.Queues[Input, Output]
  Artifacts = Artifact

  def __init__(self):
    super().__init__(Input, Output)

  def run(self, queues: Queues) -> Artifact:
    return partial(fastapi, CorrectionSDK(**queues))