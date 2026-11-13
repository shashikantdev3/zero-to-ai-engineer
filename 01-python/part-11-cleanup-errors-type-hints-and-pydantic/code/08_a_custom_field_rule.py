"""Zero to AI Engineer · Python · Part 11 of 25
Slide: A Custom Field Rule
Run: python 08_a_custom_field_rule.py
"""
# Needs: pip install pydantic
# --- repeated from 07_declaring_the_ticket_model.py so this file runs on its own ---
from typing import Literal
from pydantic import BaseModel, ConfigDict
from pydantic import Field

Cat = Literal["access", "payroll", "leave"]

class TicketBase(BaseModel):
    model_config = ConfigDict(extra="forbid")
    category: Cat
    priority: int = Field(ge=1, le=4)
    summary: str

# --- this slide ---
from pydantic import field_validator

class Ticket(TicketBase):
    @field_validator("summary")
    @classmethod
    def not_blank(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("summary is blank")
        return v.strip()
