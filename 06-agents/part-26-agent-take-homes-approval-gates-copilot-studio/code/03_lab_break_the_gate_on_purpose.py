"""Zero to AI Engineer · Agents and Tools · Part 26 of 26
Follow-along lab: Break the gate on purpose
Run: python 03_lab_break_the_gate_on_purpose.py
"""
from hashlib import sha256
h = sha256(b"refund 42").hexdigest()[:8]
rec = {"hash": h, "exp": 900, "done": False}
def resume(dec, now):
    if dec != h or now > rec["exp"]:
        return "rejected: stale or mismatched"
    if rec["done"]:
        return "skipped: already executed"
    rec["done"] = True
    return "executed refund 42"
other = sha256(b"refund 4200").hexdigest()[:8]
for dec, now in [(other, 10), (h, 1000),
                 (h, 10), (h, 20)]:
    print(resume(dec, now))
