"""Zero to AI Engineer · RAG and Vector Search · Part 1 of 26
Follow-along lab: Watch Length Change the Winner
Run: python 07_lab_watch_length_change_the_winner.py
"""
import math
def dot(a, b):
    return sum(x * y for x, y in zip(a, b))
def unit(v):
    n = math.sqrt(dot(v, v))
    return [x / n for x in v]

q = [1.0, 0.0]
a, b = [0.9, 0.1], [3.0, 2.0]
print("dot:", dot(q, a), dot(q, b))
ca, cb = dot(q, unit(a)), dot(q, unit(b))
print("cos:", round(ca, 2), round(cb, 2))
q5 = [5 * x for x in q]
print("dot x5:", dot(q5, a), dot(q5, b))
