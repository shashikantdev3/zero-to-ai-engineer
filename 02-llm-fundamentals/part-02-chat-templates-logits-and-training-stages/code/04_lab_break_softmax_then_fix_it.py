"""Zero to AI Engineer · LLM Fundamentals · Part 2 of 18
Follow-along lab: Break Softmax, Then Fix It
Run: python 04_lab_break_softmax_then_fix_it.py
"""
import math

logits = [1000.0, 999.0, 998.0]
try:
    naive = [math.exp(z) for z in logits]
    print("naive ok")
except OverflowError:
    print("naive softmax: overflow")
m = max(logits)
ex = [math.exp(z - m) for z in logits]
probs = [e / sum(ex) for e in ex]
print("probs", [round(p, 3) for p in probs])
print("sum", round(sum(probs), 3))
print("loss", round(-math.log(probs[0]), 3))
