"""Zero to AI Engineer · Prompting · Part 8 of 10
Slide: Calling with the schema
Run: python 03_calling_with_the_schema.py
"""
# Needs: pip install anthropic
# --- repeated from 01_wire_schema_and_domain_model.py, 02_making_the_schema_strict.py so this file runs on its own ---
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

schema = InvoiceOut.model_json_schema()
# strict rule: no extra keys allowed
schema["additionalProperties"] = False
# strict rule: every field is required
props = schema["properties"]
schema["required"] = list(props)
print(schema["required"])

# --- this slide ---
import anthropic
client = anthropic.Anthropic()
TEXT = "Invoice A-17, USD, total 120.50"
msgs = [{"role": "user", "content": TEXT}]
fmt = {"type": "json_schema",
       "schema": schema}
resp = client.messages.create(
    model="claude-haiku-5-5", max_tokens=300,
    thinking={"type": "disabled"},
    messages=msgs,
    output_config={"format": fmt})
text = resp.content[0].text
inv = Invoice.model_validate_json(text)
