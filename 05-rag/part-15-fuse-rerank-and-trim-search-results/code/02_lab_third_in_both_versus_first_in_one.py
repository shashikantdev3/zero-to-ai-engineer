"""Zero to AI Engineer · RAG and Vector Search · Part 15 of 26
Follow-along lab: Third in both versus first in one
Run: python 02_lab_third_in_both_versus_first_in_one.py
"""
def rrf(rankings, k=60):
    scores = {}
    for r in rankings:
        for rank, d in enumerate(r, 1):
            old = scores.get(d, 0.0)
            scores[d] = old + 1 / (k + rank)
    return scores

bm25 = ["solo", "x", "both"]
vec = ["y", "z", "both"]
s = rrf([bm25, vec])
print("solo:", round(s["solo"], 4))
print("both:", round(s["both"], 4))
print("winner:", max(s, key=s.get))
