"""Zero to AI Engineer · Agents and Tools · Part 10 of 26
Slide: A gate with no confidence input
Run: python 01_a_gate_with_no_confidence_input.py
"""
from dataclasses import dataclass
@dataclass
class Action:
    risk: str
    writes_system_of_record: bool = False

RISKY = {"irreversible", "customer_visible",
         "money"}

def needs_human(action: Action) -> bool:
    return (action.risk in RISKY
        or action.writes_system_of_record)
