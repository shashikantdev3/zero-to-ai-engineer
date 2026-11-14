"""Zero to AI Engineer · Agents and Tools · Part 10 of 26
Slide: Checkpoint and release the worker
Run: python 03_checkpoint_and_release_the_worker.py
"""
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
