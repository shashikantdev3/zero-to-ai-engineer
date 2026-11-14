"""Zero to AI Engineer · Agents and Tools · Part 10 of 26
Slide: Resume, expire, apply once
Run: python 04_resume_expire_apply_once.py
"""
# --- repeated from 03_checkpoint_and_release_the_worker.py so this file runs on its own ---
import json
from datetime import datetime, timedelta

# state lives outside the process
store = {}
run = {"incident": "INC-42",
       "plan": "restart api",
       "asked": "2025-01-06T09:00",
       "decision": None}
store["run-1"] = json.dumps(run)
# checkpoint saved, worker released

# --- this slide ---
applied = set()
def resume(run_id, signed, now):
    run = json.loads(store[run_id])
    asked = datetime.fromisoformat(run["asked"])
    if now - asked > timedelta(hours=4):
        return "approval expired"
    if run_id in applied:
        return "already applied"
    applied.add(run_id)
    return f"applied {run['plan']} by {signed}"
t = datetime(2025, 1, 6, 10, 0)
print(resume("run-1", "ops", t))
