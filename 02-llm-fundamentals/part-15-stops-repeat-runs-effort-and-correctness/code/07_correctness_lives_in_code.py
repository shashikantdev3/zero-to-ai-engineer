"""Zero to AI Engineer · LLM Fundamentals · Part 15 of 18
Slide: Correctness Lives in Code
Run: python 07_correctness_lives_in_code.py
"""
# --- repeated from 06_define_the_shape_exactly.py so this file runs on its own ---
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

# --- this slide ---
raw = ('{"items": [{"description": "Desk",'
       ' "amount": "120.50"}],'
       ' "tax": "24.10", "total": "150.00"}')
# shape check, amounts become Decimal
inv = Invoice.model_validate_json(raw)
total = sum(i.amount for i in inv.items)
# business rule, explicit if, not assert
if total + inv.tax != inv.total:
    print("send to human review")
