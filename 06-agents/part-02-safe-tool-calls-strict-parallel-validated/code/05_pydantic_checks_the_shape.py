"""Zero to AI Engineer · Agents and Tools · Part 2 of 26
Slide: Pydantic checks the shape
Run: python 05_pydantic_checks_the_shape.py
"""
# Needs: pip install pydantic
from pydantic import BaseModel, Field
from pydantic import ValidationError

ID_RE = r"^ORD-\d{6}$"

class RefundArgs(BaseModel):
    order_id: str = Field(pattern=ID_RE)
    amount_inr: int = Field(gt=0, le=50_000)

orders = {"ORD-123456": "u1"}
def fail(code):
    return {"ok": False, "error": code}
