"""Zero to AI Engineer · Agents and Tools · Part 6 of 26
Slide: The plan as a typed object
Run: python 05_the_plan_as_a_typed_object.py
"""
# Needs: pip install pydantic
from typing import Literal
from pydantic import BaseModel
class Step(BaseModel):
    action: Literal["look", "request_change"]
    target: str
    reason: str
class Plan(BaseModel):
    incident_id: str
    steps: list[Step]
s = Step(action="request_change",
         target="db", reason="restart")
plan = Plan(incident_id="INC-7", steps=[s])
