"""Zero to AI Engineer · Security and Guardrails · Part 10 of 11
Follow-along lab: Catch a Rewrite With an Anchor
Run: python 05_lab_catch_a_rewrite_with_an_anchor.py
"""
from hashlib import sha256
def head(events: list[str]) -> str:
    prev = "0" * 64
    for ev in events:
        data = (prev + ev).encode()
        prev = sha256(data).hexdigest()
    return prev
log = ["login", "ask", "approve"]
anchor = head(log)
print("anchor:", anchor[:12])
print("before edit:", head(log) == anchor)
log[2] = "deny"
print("rewritten:", head(log)[:12])
print("after edit:", head(log) == anchor)
