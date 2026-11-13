"""Zero to AI Engineer · Python · Part 11 of 25
Slide: Validate, Dump, or Collect Errors
Run: python 09_validate_dump_or_collect_errors.py
"""
# Needs: pip install pydantic
# --- repeated from 07_declaring_the_ticket_model.py, 08_a_custom_field_rule.py so this file runs on its own ---
from typing import Literal
from pydantic import BaseModel, ConfigDict
from pydantic import Field

Cat = Literal["access", "payroll", "leave"]

class TicketBase(BaseModel):
    model_config = ConfigDict(extra="forbid")
    category: Cat
    priority: int = Field(ge=1, le=4)
    summary: str

from pydantic import field_validator

class Ticket(TicketBase):
    @field_validator("summary")
    @classmethod
    def not_blank(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("summary is blank")
        return v.strip()

# --- this slide ---
from pydantic import ValidationError

raw = ('{"category": "access", "priority": 2,'
       ' "summary": " VPN locked "}')
try:
    t = Ticket.model_validate_json(raw)
    print(t.model_dump())
except ValidationError as e:
    # send back for one bounded retry
    feedback = e.errors()
