"""Zero to AI Engineer · Agents and Tools · Part 25 of 26
Slide: Errors and the fingerprint
Run: python 03_errors_and_the_fingerprint.py
"""
import hashlib, json

END = "__end__"
class StepLimit(Exception): pass
class CycleDetected(Exception): pass
class UnknownNode(Exception): pass

def fingerprint(node, state):
    raw = json.dumps(state, sort_keys=True,
                     default=str).encode()
    return (node,
            hashlib.sha256(raw).hexdigest())
