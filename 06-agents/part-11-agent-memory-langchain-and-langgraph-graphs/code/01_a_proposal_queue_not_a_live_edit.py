"""Zero to AI Engineer · Agents and Tools · Part 11 of 26
Slide: A proposal queue, not a live edit
Run: python 01_a_proposal_queue_not_a_live_edit.py
"""
from dataclasses import dataclass

@dataclass
class ProcUpdate:
    rule: str
    evidence_run_id: str
    # proposed, approved, merged into Git
    status: str = "proposed"

def propose(rule, run_id, queue):
    # Append only. Never edit live prompt.
    queue.append(ProcUpdate(rule, run_id))
