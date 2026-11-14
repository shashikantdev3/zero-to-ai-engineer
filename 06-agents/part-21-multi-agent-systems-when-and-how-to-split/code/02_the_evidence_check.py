"""Zero to AI Engineer · Agents and Tools · Part 21 of 26
Slide: The evidence check
Run: python 02_the_evidence_check.py
"""
# Needs: pip install pydantic
# --- repeated from 01_the_finding_schema.py so this file runs on its own ---
from pydantic import BaseModel, Field

MIN_QUOTE = 12

class Finding(BaseModel):
    incident_id: str
    claim: str = Field(min_length=1)
    # must appear verbatim in the evidence
    quote: str = Field(min_length=MIN_QUOTE)
    source_id: str = Field(min_length=1)

# --- this slide ---
def norm(s: str) -> str:
    # collapse whitespace, keep case exact
    return " ".join(s.split())
def assay(f: Finding, ev: dict[str, str]):
    if f.source_id not in ev:
        return False, "unknown source_id"
    q = norm(f.quote)
    if len(q) < MIN_QUOTE:
        return False, "quote too short"
    if q not in norm(ev[f.source_id]):
        return False, "not found verbatim"
    return True, "ok"
