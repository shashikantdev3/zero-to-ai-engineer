"""Zero to AI Engineer · Python · Part 11 of 25
Slide: Declaring the Ticket Model
Run: python 07_declaring_the_ticket_model.py
"""
# Needs: pip install pydantic
from typing import Literal
from pydantic import BaseModel, ConfigDict
from pydantic import Field

Cat = Literal["access", "payroll", "leave"]

class TicketBase(BaseModel):
    model_config = ConfigDict(extra="forbid")
    category: Cat
    priority: int = Field(ge=1, le=4)
    summary: str
