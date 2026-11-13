"""Zero to AI Engineer · Prompting · Part 8 of 10
Slide: Wire schema and domain model
Run: python 01_wire_schema_and_domain_model.py
"""
# Needs: pip install pydantic
from decimal import Decimal
from typing import Literal
from pydantic import BaseModel

class InvoiceOut(BaseModel):
    invoice_no: str
    currency: Literal["INR", "USD", "EUR"]
    # string on the wire, Decimal in code
    total: str

class Invoice(InvoiceOut):
    total: Decimal
