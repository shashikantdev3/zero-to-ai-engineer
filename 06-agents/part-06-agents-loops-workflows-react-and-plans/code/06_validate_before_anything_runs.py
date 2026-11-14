"""Zero to AI Engineer · Agents and Tools · Part 6 of 26
Slide: Validate before anything runs
Run: python 06_validate_before_anything_runs.py
"""
# Needs: pip install pydantic
# --- repeated from 05_the_plan_as_a_typed_object.py so this file runs on its own ---
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

# --- this slide ---
ALLOWED = {"cache", "web-1"}
def validate_plan(p: Plan) -> list[str]:
    errs = []
    if len(p.steps) > 6:
        errs.append("too many steps")
    for s in p.steps:
        if (s.action == "request_change"
                and s.target not in ALLOWED):
            errs.append("non-allowed target")
    return errs
print(validate_plan(plan))
