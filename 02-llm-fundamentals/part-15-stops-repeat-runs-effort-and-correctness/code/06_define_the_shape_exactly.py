"""Zero to AI Engineer · LLM Fundamentals · Part 15 of 18
Slide: Define the Shape Exactly
Run: python 06_define_the_shape_exactly.py
"""
# Needs: pip install pydantic
from decimal import Decimal
from pydantic import BaseModel

class Item(BaseModel):
    description: str
    # model returns "120.50", parsed exactly
    amount: Decimal

class Invoice(BaseModel):
    items: list[Item]
    tax: Decimal
    total: Decimal
