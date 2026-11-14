"""Zero to AI Engineer · Agents and Tools · Part 11 of 26
Follow-along lab: Build a tiny reducer merge
Run: python 07_lab_build_a_tiny_reducer_merge.py
"""
from operator import add
REDUCERS = {"findings": add}
def merge(state, update):
    new = dict(state)
    for k, v in update.items():
        f = REDUCERS.get(k)
        new[k] = f(new[k], v) if f else v
    return new
s = {"findings": [], "steps": 0}
a = merge(s, {"findings": ["db"], "steps": 1})
print(a["findings"], a["steps"])
b = merge(a, {"findings": ["io"], "steps": 2})
print(b["findings"], b["steps"])
print(s)
