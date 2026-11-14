"""Zero to AI Engineer · RAG and Vector Search · Part 22 of 26
Slide: A closed schema in Pydantic
Run: python 01_a_closed_schema_in_pydantic.py
"""
# Needs: pip install pydantic
from typing import Literal
from pydantic import BaseModel
Kind = Literal["Service", "Team", "Runbook"]
Rel = Literal["DEPENDS_ON", "OWNED_BY",
              "DOCUMENTED_IN"]
class Edge(BaseModel):
    source: str
    source_type: Kind
    relation: Rel
    target: str
    target_type: Kind
    chunk_id: str  # provenance
