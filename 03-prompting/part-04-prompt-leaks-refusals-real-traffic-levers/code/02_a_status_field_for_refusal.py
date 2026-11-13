"""Zero to AI Engineer · Prompting · Part 4 of 10
Slide: A Status Field for Refusal
Run: python 02_a_status_field_for_refusal.py
"""
# Needs: pip install pydantic
from typing import Literal
from pydantic import BaseModel

class Answer(BaseModel):
    # Domain model. The strict-mode wire
    # schema has no defaults.
    status: Literal["answered",
                    "not_found",
                    "needs_human"]
    text: str | None
    citations: list[str] = []
