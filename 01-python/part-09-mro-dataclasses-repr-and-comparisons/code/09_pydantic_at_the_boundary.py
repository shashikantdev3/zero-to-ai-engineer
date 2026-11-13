"""Zero to AI Engineer · Python · Part 9 of 25
Slide: Pydantic at the boundary
Run: python 09_pydantic_at_the_boundary.py
"""
# Needs: pip install pydantic
from pydantic import BaseModel

# boundary: validates and coerces
class ChunkIn(BaseModel):
    doc_id: str
    score: float = 0.0

d = {"doc_id": "d1", "score": "0.82"}
print(ChunkIn.model_validate(d).score)
