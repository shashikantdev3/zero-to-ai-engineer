"""Zero to AI Engineer · Agents and Tools · Part 22 of 26
Follow-along lab: Why timestamps break the guard
Run: python 08_lab_why_timestamps_break_the_guard.py
"""
import hashlib, json

def fp(d):
    b = json.dumps(d, sort_keys=True).encode()
    return hashlib.sha256(b).hexdigest()[:8]

whole, prog = set(), set()
for ts in (101, 102, 103):
    s = {"findings": ["disk full"], "ts": ts}
    p = fp(s["findings"])
    print(ts, "whole:", fp(s) in whole,
          "progress:", p in prog)
    whole.add(fp(s)); prog.add(p)
