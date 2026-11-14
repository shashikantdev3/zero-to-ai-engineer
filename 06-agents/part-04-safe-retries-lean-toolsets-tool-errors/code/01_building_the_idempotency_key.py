"""Zero to AI Engineer · Agents and Tools · Part 4 of 26
Slide: Building the idempotency key
Run: python 01_building_the_idempotency_key.py
"""
import hashlib, json

def sha(text):
    return hashlib.sha256(
        text.encode()).hexdigest()

def idem_key(inc, plan, step, action, args):
    a = json.dumps(args, sort_keys=True,
                   separators=(",", ":"))
    return sha(f"{inc}:{plan}:{step}"
               f":{action}:{sha(a)}")
