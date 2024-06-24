from typing_extensions import TypedDict, NotRequired
from pipeteer import Task
from dslog import Logger
from fastapi import FastAPI
from ._types import Input, Output
from .api import fastapi
from .sdk import CorrectionSDK

class Params(TypedDict):
  images_path: NotRequired[str | None]
  logger: Logger

class GameCorrection(Task[Input, Output, Params, FastAPI]):
  Queues = Task.Queues[Input, Output]
  Params = Params
  Artifacts = FastAPI

  def __init__(self):
    super().__init__(Input, Output)

  def run(self, queues: Queues, params: Params):
    return fastapi(CorrectionSDK(**queues), **params)