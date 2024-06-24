from typing_extensions import TypeAlias, Sequence, Coroutine
from dataclasses import dataclass
from functools import partial
from dslog import Logger
from kv.api import KV
from pipeteer import Task
import tf.serving as tfs

@dataclass
class Input:
  ply_boxes: Sequence[Sequence[str]]
  endpoint: str | None = None

Preds: TypeAlias = Sequence[Sequence[Sequence[tuple[str, float]]]]

class Params(tfs.Params):
  blobs: KV[bytes]
  logger: Logger

class OCRPredict(Task[Input, Preds, Params, Coroutine]):
  Queues = Task.Queues[Input, Preds]
  Input = Input
  Output = Preds
  Params = Params
  Artifacts = Coroutine

  def __init__(self):
    super().__init__(Input, Preds)

  def run(self, queues: Queues, params: Params):
    from .main import run
    return run(**queues, **params)