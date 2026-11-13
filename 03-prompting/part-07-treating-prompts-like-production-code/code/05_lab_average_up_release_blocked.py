"""Zero to AI Engineer · Prompting · Part 7 of 10
Follow-along lab: Average Up, Release Blocked
Run: python 05_lab_average_up_release_blocked.py
"""
old = {"vpn": 1, "reset": 0,
       "billing": 0, "outage": 1}
new = {"vpn": 1, "reset": 1,
       "billing": 1, "outage": 0}
critical = {"outage"}
print("old passes:", sum(old.values()))
print("new passes:", sum(new.values()))
regs = [c for c in old
        if old[c] and not new[c]]
print("regressions:", regs)
bad = [c for c in regs if c in critical]
print("blocked:" if bad else "ship:", bad)
