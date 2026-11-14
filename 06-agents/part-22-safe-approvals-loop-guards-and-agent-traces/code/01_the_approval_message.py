"""Zero to AI Engineer · Agents and Tools · Part 22 of 26
Slide: The approval message
Run: python 01_the_approval_message.py
"""
import hashlib, json

def canonical(obj) -> bytes:
    # stable in one Python service only
    return json.dumps(obj, sort_keys=True,
        separators=(",", ":")).encode()

def approval_msg(inc, plan, meta):
    data = canonical(plan)
    h = hashlib.sha256(data).hexdigest()
    return canonical({"incident": inc,
        "plan_sha256": h, **meta})
