"""Zero to AI Engineer · Agents and Tools · Part 10 of 26
Follow-along lab: Measure your approval gate
Run: python 02_lab_measure_your_approval_gate.py
"""
from statistics import median
# (decision, seconds to approve)
log = [("ok", 2), ("ok", 3), ("ok", 2),
       ("ok", 4), ("ok", 3), ("ok", 2)]
rej = [d for d, s in log if d == "no"]
rate = len(rej) / len(log)
p50 = median(s for d, s in log)
print(f"reviewed: {len(log)}")
print(f"rejection rate: {rate:.0%}")
print(f"p50 seconds: {p50}")
flag = rate == 0 or p50 < 10
print(f"rubber stamp? {flag}")
pending_hours = 30
print(f"expired: {pending_hours > 4}")
