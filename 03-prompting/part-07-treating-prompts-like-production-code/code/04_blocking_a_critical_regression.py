"""Zero to AI Engineer · Prompting · Part 7 of 10
Slide: Blocking a Critical Regression
Run: python 04_blocking_a_critical_regression.py
"""
# Note: this stops on purpose with a message. The video explains why.
import sys

# True means the case is critical
cases = {"vpn": False, "outage": True}
old = {"vpn": True, "outage": True}
new = {"vpn": True, "outage": False}

regressions = [c for c in cases
               if old[c] and not new[c]]
if any(cases[c] for c in regressions):
    sys.exit("Blocked: critical regression")
print("Release allowed")
