from typing import Sequence
from dataclasses import dataclass
import moveread.pipelines.preprocess as pre

@dataclass
class Input:
  model: str
  imgs: Sequence[str]

@dataclass
class Game:
  model: str
  imgIds: Sequence[str]

Output = Sequence[pre.Output]