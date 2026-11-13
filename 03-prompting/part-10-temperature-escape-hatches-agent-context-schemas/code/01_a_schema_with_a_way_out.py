"""Zero to AI Engineer · Prompting · Part 10 of 10
Slide: A schema with a way out
Run: python 01_a_schema_with_a_way_out.py
"""
# Needs: pip install pydantic
from typing import Literal
from pydantic import BaseModel

class Extracted(BaseModel):
    status: Literal[
        "extracted",
        "not_found",
        "needs_review",
    ]
    po_number: str | None
    # exact quote from the source
    po_evidence: str | None
