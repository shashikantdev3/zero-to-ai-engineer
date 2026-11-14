"""Zero to AI Engineer · Agents and Tools · Part 22 of 26
Slide: The loop guard in code
Run: python 07_the_loop_guard_in_code.py
"""
import hashlib, json
TRACK = "findings plan open_questions".split()
def on_handoff(task, state, limit=6):
    task["handoffs"] += 1
    prog = {k: state.get(k) for k in TRACK}
    raw = json.dumps(prog, sort_keys=True,
                     default=str).encode()
    h = hashlib.sha256(raw).hexdigest()
    over = task["handoffs"] > limit
    if over or h in task["seen"]:
        return "escalate: no progress"
    task["seen"].add(h)
