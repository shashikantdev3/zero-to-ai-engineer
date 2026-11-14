"""Zero to AI Engineer · Security and Guardrails · Part 6 of 11
Follow-along lab: Watch a semantic cache leak
Run: python 05_lab_watch_a_semantic_cache_leak.py
"""
import math
def sim(a, b):
    d = sum(x * y for x, y in zip(a, b))
    return d / math.hypot(*a) / math.hypot(*b)
cache = [("A", (0.9, 0.1), "A refund terms")]
def lookup(q, tenant=None):
    for t, v, ans in cache:
        ok = tenant is None or t == tenant
        if ok and sim(q, v) >= 0.95:
            return ans
q = (0.88, 0.12)
print("shared:", lookup(q))
print("scoped to B:", lookup(q, "B"))
print("scoped to A:", lookup(q, "A"))
