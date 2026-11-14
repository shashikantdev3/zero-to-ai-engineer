"""Zero to AI Engineer · RAG and Vector Search · Part 22 of 26
Slide: Off-schema output fails
Run: python 02_off_schema_output_fails.py
"""
# Needs: pip install pydantic
# --- repeated from 01_a_closed_schema_in_pydantic.py so this file runs on its own ---
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

# --- this slide ---
class Extraction(BaseModel):
    edges: list[Edge]
raw = ('{"edges": [{"source": "checkout",'
       ' "source_type": "Service",'
       ' "relation": "WORKS_WITH",'
       ' "target": "payments",'
       ' "target_type": "Service",'
       ' "chunk_id": "c-17"}]}')
try:
    Extraction.model_validate_json(raw)
except ValueError as err:
    print("rejected:", err.error_count())
