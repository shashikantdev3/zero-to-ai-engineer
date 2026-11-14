"""Zero to AI Engineer · Agents and Tools · Part 7 of 26
Slide: The run state
Run: python 01_the_run_state.py
"""
import json
from dataclasses import dataclass, field
MAX_STEPS, MAX_USD = 12, 0.05
POLL_TOOLS = {"get_job_status": 10}
class Stop(Exception): pass
# one per run, never module-level
@dataclass
class RunState:
    step: int = 0
    spent_usd: float = 0.0
    last_sig: tuple | None = None
    polls: dict = field(default_factory=dict)
