"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 20 of 28
Slide: Retrieve, then rank
Run: python 04_retrieve_then_rank.py
"""
# --- repeated from 03_stage_one_helper_cosine_top_k.py so this file runs on its own ---
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

# --- this slide ---
items = {"a": [1, 0], "b": [0.9, 0.1],
         "c": [0, 1], "d": [0.7, 0.7]}
user, user_vec = "u1", [1, 0.2]
class Ranker:
    def score(self, user, item):
        return {"b": 9, "d": 6}.get(item, 0)
ranker = Ranker()
# stage 1: cheap retrieval
cand = top_k(user_vec, items, k=3)
# stage 2: expensive ranking
ranked = sorted(cand, key=lambda c:
    -ranker.score(user, c[0]))
