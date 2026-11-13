"""Zero to AI Engineer · Python · Part 9 of 25
Slide: Ordering on one field
Run: python 03_ordering_on_one_field.py
"""
from dataclasses import dataclass, field

@dataclass(order=True)
class Scored:
    score: float
    doc_id: str = field(compare=False)
    tags: list[str] = field(
        default_factory=list, compare=False)

a = Scored(0.9, "d1")
b = Scored(0.4, "d2")
print(sorted([a, b])[0].doc_id)
