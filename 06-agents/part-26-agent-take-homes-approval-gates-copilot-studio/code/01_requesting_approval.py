"""Zero to AI Engineer · Agents and Tools · Part 26 of 26
Slide: Requesting approval
Run: python 01_requesting_approval.py
"""
import json, time, pathlib
PENDING = pathlib.Path("pending")

def request_approval(run_id, action,
                     plan_hash, state):
    PENDING.mkdir(exist_ok=True)
    rec = {"action": action, "state": state,
           "plan_hash": plan_hash,
           "exp": time.time() + 900}
    path = PENDING / f"{run_id}.json"
    path.write_text(json.dumps(rec))
    return "awaiting_approval"
