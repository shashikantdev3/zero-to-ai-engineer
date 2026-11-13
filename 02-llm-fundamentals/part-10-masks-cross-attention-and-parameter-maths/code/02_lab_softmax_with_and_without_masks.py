"""Zero to AI Engineer · LLM Fundamentals · Part 10 of 18
Follow-along lab: Softmax with and without masks
Run: python 02_lab_softmax_with_and_without_masks.py
"""
import math

def softmax(row):
    m = max(row)
    e = [math.exp(s - m) for s in row]
    return [round(v / sum(e), 2) for v in e]

inf = float("inf")
print("raw:", softmax([2.0, 1.0, 0.5]))
print("zero:", softmax([2.0, 1.0, 0.0]))
print("finite:", softmax([2.0, 1.0, -1e9]))
print("empty:", softmax([-1e9, -1e9]))
print("inf row:", softmax([-inf, -inf]))
