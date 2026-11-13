"""Zero to AI Engineer · Prompting · Part 10 of 10
Slide: Descriptions written as rules
Run: python 04_descriptions_written_as_rules.py
"""
# Needs: pip install pydantic
from typing import Literal
from pydantic import BaseModel, Field

Cur = Literal["INR", "USD", "EUR"]

class Invoice(BaseModel):
    amount: str = Field(description=(
        "Amount as digits and a dot, "
        "no thousands separators, "
        "e.g. 1250.00"))
    currency: Cur = Field(description=(
        "ISO code printed on the invoice"))
