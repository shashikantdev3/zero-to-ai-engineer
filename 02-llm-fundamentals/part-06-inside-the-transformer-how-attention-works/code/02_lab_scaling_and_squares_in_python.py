"""Zero to AI Engineer · LLM Fundamentals · Part 6 of 18
Follow-along lab: Scaling and squares in Python
Run: python 02_lab_scaling_and_squares_in_python.py
"""
import math
def softmax(xs):
    m = max(xs)
    e = [math.exp(x - m) for x in xs]
    t = sum(e)
    return [round(v / t, 3) for v in e]
raw = [24.0, 16.0, 8.0]
d_k = 64
print("raw:", softmax(raw))
scaled = [x / math.sqrt(d_k) for x in raw]
print("scaled:", softmax(scaled))
for n in (8000, 16000):
    print(n, "tokens:", n * n, "scores")
