from typing import TypeAlias, Sequence, Protocol, Unpack
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

class Artifact(Protocol):
  async def __call__(self, *, blobs: KV[bytes], logger: Logger | None = None, **params: Unpack[tfs.Params]):
    ...

class OCRPredict(Task[Input, Preds, Artifact]):
  Queues = Task.Queues[Input, Preds]
  Artifacts = Artifact

  def __init__(self):
    super().__init__(Input, Preds)

  def run(self, queues: Queues) -> Artifact:
    from .main import run
    return partial(run, **queues)