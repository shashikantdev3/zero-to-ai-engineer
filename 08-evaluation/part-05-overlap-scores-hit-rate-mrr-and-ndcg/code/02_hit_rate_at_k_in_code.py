"""Zero to AI Engineer · Evaluation · Part 5 of 11
Slide: Hit rate at k in code
Run: python 02_hit_rate_at_k_in_code.py
"""
def hit_rate_at_k(results, expected, k=5):
    # skip must-abstain cases
    pairs = [(g, e) for g, e
             in zip(results, expected) if e]
    hits = sum(1 for g, e in pairs
               if e & set(g[:k]))
    if not pairs:
        return float("nan")
    return hits / len(pairs)
