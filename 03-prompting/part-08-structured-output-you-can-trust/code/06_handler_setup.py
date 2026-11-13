"""Zero to AI Engineer · Prompting · Part 8 of 10
Slide: Handler setup
Run: python 06_handler_setup.py
"""
# Needs: pip install pydantic
import re
from pydantic import BaseModel
from pydantic import ValidationError
TICKET_ID = re.compile(r"INC[0-9]{7}")
class TicketArgs(BaseModel):
    ticket_id: str
