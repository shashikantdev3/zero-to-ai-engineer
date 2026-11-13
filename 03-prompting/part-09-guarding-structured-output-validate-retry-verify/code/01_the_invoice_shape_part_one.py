"""Zero to AI Engineer · Prompting · Part 9 of 10
Slide: The invoice shape, part one
Run: python 01_the_invoice_shape_part_one.py
"""
# Needs: pip install pydantic
from decimal import Decimal
from typing import Literal
from pydantic import BaseModel, Field
from pydantic import field_validator

class Line(BaseModel):
    description: str = Field(max_length=200)
    amount: Decimal = Field(ge=0)
