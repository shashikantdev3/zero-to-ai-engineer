"""Zero to AI Engineer · Python · Part 9 of 25
Slide: TypedDict, NamedTuple, dataclass
Run: python 08_typeddict_namedtuple_dataclass.py
"""
from typing import NamedTuple, TypedDict
from dataclasses import dataclass
class ChunkTD(TypedDict):
    doc_id: str
    score: float
class ChunkNT(NamedTuple):
    doc_id: str
    score: float = 0.0
@dataclass(frozen=True, slots=True)
class ChunkDC:
    doc_id: str
    tags: tuple[str, ...] = ()
