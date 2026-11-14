"""Zero to AI Engineer · Evaluation · Part 6 of 11
Slide: Rank-weighted context precision
Run: python 01_rank_weighted_context_precision.py
"""
def context_precision_at_k(flags, k):
    # flags[i]: is chunk i relevant?
    # rank-weighted precision
    score, hits = 0.0, 0
    for i, rel in enumerate(flags[:k], 1):
        if rel:
            hits += 1
            score += hits / i
    return score / hits if hits else 0.0

flags = [True, False, True]
print(context_precision_at_k(flags, 3))
