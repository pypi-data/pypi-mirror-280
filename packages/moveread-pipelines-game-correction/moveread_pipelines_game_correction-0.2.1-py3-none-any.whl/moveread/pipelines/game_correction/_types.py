from typing import Literal, Self, Sequence
import os
from dataclasses import dataclass, replace, field
from game_prediction2 import Annotations as PredAnnotations
from chess_notation.language import Language
from chess_notation.styles import PawnCapture, PieceCapture

NA = Literal['N/A']
def no_na(value):
  if value != 'N/A':
    return value

@dataclass
class Annotations:
  lang: Language | NA | None = None
  pawn_capture: PawnCapture | NA | None = None
  piece_capture: PieceCapture | NA | None = None
  end_correct: int | None = None

  def for_preds(self) -> 'PredAnnotations':
    """Convert to `game_correction.Annotations` (replaces `'N/A'`s with `None`s)"""
    return PredAnnotations(
      lang=no_na(self.lang),
      pawn_capture=no_na(self.pawn_capture),
      piece_capture=no_na(self.piece_capture),
    )
  
@dataclass
class Meta:
  title: str | None = None
  details: str | None = None

@dataclass(kw_only=True)
class BaseInput(Meta):
  ply_boxes: Sequence[Sequence[str]]
  annotations: Sequence[Annotations] | None = None

  def at_url(self, images_path: str) -> 'Self':
    copy = replace(self)
    copy.ply_boxes = [
      [os.path.join(images_path, box) for box in boxes]
      for boxes in self.ply_boxes
    ]
    return copy

@dataclass(kw_only=True)
class Input(BaseInput):
  ocrpreds: Sequence[Sequence[Sequence[tuple[str, float]]]]
  """BATCH x PLAYERS x TOP_PREDS x (word, logprob)"""

@dataclass
class CorrectResult:
  annotations: Sequence[Annotations]
  pgn: Sequence[str]
  early: bool
  tag: Literal['correct'] = field(default='correct', kw_only=True)

@dataclass
class BadlyPreprocessed:
  tag: Literal['badly-preprocessed'] = 'badly-preprocessed'

@dataclass
class Output:
  output: CorrectResult | BadlyPreprocessed

@dataclass(kw_only=True)
class MetaItem(Meta):
  id: str

@dataclass(kw_only=True)
class Item(BaseInput):
  id: str
  pgn: Sequence[str] | None = None
  manual_ucis: dict[int, str] | None = None
