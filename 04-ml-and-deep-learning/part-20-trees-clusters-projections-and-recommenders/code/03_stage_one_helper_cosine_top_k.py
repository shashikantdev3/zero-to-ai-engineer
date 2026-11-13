"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 20 of 28
Slide: Stage one helper: cosine top k
Run: python 03_stage_one_helper_cosine_top_k.py
"""
import math
def cos(a, b):
    d = sum(x * y for x, y in zip(a, b))
    n = math.hypot(*a) * math.hypot(*b)
    return d / n
def top_k(u, items, k):
    s = [(i, cos(u, v))
         for i, v in items.items()]
    s.sort(key=lambda c: -c[1])
    return s[:k]
