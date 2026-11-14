"""Zero to AI Engineer · Agents and Tools · Part 21 of 26
Slide: The Finding schema
Run: python 01_the_finding_schema.py
"""
# Needs: pip install pydantic
from pydantic import BaseModel, Field

MIN_QUOTE = 12

class Finding(BaseModel):
    incident_id: str
    claim: str = Field(min_length=1)
    # must appear verbatim in the evidence
    quote: str = Field(min_length=MIN_QUOTE)
    source_id: str = Field(min_length=1)
