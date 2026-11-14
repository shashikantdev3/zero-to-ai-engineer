"""Zero to AI Engineer · Security and Guardrails · Part 6 of 11
Slide: Validating an action with Pydantic
Run: python 08_validating_an_action_with_pydantic.py
"""
# Needs: pip install pydantic
from pydantic import BaseModel, Field
class Action(BaseModel):
    ticket_id: str = Field(
        pattern=r"^INC\d{7}$")
    # no 'closed' for the bot
    status: str = Field(
        pattern=r"^(open|pending)$")
raw = ('{"ticket_id": "INC0012345",'
       ' "status": "open"}')
# raises on anything else
action = Action.model_validate_json(raw)
print(action.status)
