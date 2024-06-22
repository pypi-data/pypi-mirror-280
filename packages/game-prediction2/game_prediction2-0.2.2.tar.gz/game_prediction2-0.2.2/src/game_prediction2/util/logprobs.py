from typing import Sequence
from itertools import zip_longest
from editdistance import distance as edit_dist
import numpy as np
from pydantic import BaseModel
from chess_notation import representations, Language, MotionStyles, PawnCapture, PieceCapture, CapturedPiece
from ..beam import Logprob

def pseudo_logp(word: str, top_preds: Sequence[tuple[str, float]]) -> float:
  """Approximates the log probability of `word` given a subset of the best outputs `top_preds` of a model.
  - `top_preds :: [(Pred, Logprob)]`: the top-k predictions of a model with probability distribution `P`
    - So, each `(pred, logp) in top_preds` holds `logp = log P(pred)`
  - If `word` is in `top_preds`, the real log-probability is returned
  - Otherwise, an approximation factor `alpha(p)` is computed as `1 - NED(word, p)` for every `p in preds`
    - `NED` is the Normalized Edit Distance (normalized over `len(word)`)
    - If `NED(word, p) <= 1`, the assigned probability is `P(p)*alpha(p)`
    - Otherwise, the probability is 0
  - The maximum across all computed probabilities is returned
  
  **Note: both computations and the returned value are indeed log-probabilities. The explanation talks normal probabilities for clarity**
  """
  return max(
    (np.log(1 - dist/len(word)) + logp
    for pred, logp in top_preds if (dist := edit_dist(pred, word)) < min(len(word), len(pred))),
    default=-float('inf')
  )
  

class Annotations(BaseModel):
  lang: Language | None = None
  pawn_capture: PawnCapture | None = None
  piece_capture: PieceCapture | None = None

  def motions(self) -> MotionStyles:
    styles = MotionStyles()
    if self.pawn_capture: styles.pawn_captures = [self.pawn_capture]
    if self.piece_capture: styles.piece_captures = [self.piece_capture]
    return styles
  
  def langs(self) -> list[Language] | None:
    if self.lang is not None:
      return [self.lang]
    
def max_pseudo_logp(san: str, captured_piece: CapturedPiece | None, top_preds: Sequence[tuple[str, float]], ann: Annotations) -> float:
  """Max `pseudo_logp` across all possible representations of `san`"""
  reprs = representations(san, motions=ann.motions(), captured_piece=captured_piece, languages=ann.langs() or ['CA', 'EN'])
  return max(pseudo_logp(r, top_preds) for r in reprs)

def players_max_pseudo_logp(san: str, captured_piece: CapturedPiece | None, players_preds: Sequence[Sequence[tuple[str, float]]], annotations: Sequence[Annotations] | None = None) -> float:
  """Max `max_pseudo_logp` across players"""
  annotations = annotations or [Annotations() for _ in players_preds]
  return max(
    max_pseudo_logp(san, captured_piece, preds, ann or Annotations())
    for preds, ann in zip_longest(players_preds, annotations)
      if preds is not None
  )

def logprob(players_preds: Sequence[Sequence[tuple[str, float]]], annotations: Sequence[Annotations] | None = None) -> Logprob:
  """Curried version of `players_max_pseudo_logp`"""
  def _logprob(san: str, captured_piece: CapturedPiece | None):
    return players_max_pseudo_logp(san, captured_piece, players_preds, annotations)
  return _logprob
  
def weighted_geo_mean(logp: float, logq: float, a: float, b: float):
  """Weighted geometrical mean (`[p^a * q^b]^(1/(a+b))`) but in log-space"""
  return (a*logp + b*logq) / (a+b)