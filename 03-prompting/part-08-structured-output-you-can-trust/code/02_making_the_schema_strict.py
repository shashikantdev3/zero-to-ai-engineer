"""Zero to AI Engineer · Prompting · Part 8 of 10
Slide: Making the schema strict
Run: python 02_making_the_schema_strict.py
"""
# --- repeated from 01_wire_schema_and_domain_model.py so this file runs on its own ---
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

# --- this slide ---
schema = InvoiceOut.model_json_schema()
# strict rule: no extra keys allowed
schema["additionalProperties"] = False
# strict rule: every field is required
props = schema["properties"]
schema["required"] = list(props)
print(schema["required"])
