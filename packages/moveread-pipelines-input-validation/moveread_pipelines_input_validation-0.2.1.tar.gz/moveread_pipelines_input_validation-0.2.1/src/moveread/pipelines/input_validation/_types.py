from typing_extensions import Sequence, TypedDict
from dataclasses import dataclass, replace
import os

class GameId(TypedDict):
  group: str
  round: str
  board: str

@dataclass
class Input:
  gameId: GameId
  imgs: Sequence[str]

@dataclass
class Item(Input):
  taskId: str

  def at_url(self, base_url: str) -> 'Item':
    copy = replace(self)
    copy.imgs = [os.path.join(base_url, img) for img in self.imgs]
    return copy

@dataclass
class Output:
  gameId: GameId
  imgs: Sequence[str]

  def strip_url(self, base_url: str) -> 'Output':
    copy = replace(self)
    copy.imgs = [img.replace(base_url, '').strip('/') for img in self.imgs]
    return copy