"""Zero to AI Engineer · Evaluation · Part 5 of 11
Slide: Recall at k in code
Run: python 03_recall_at_k_in_code.py
"""
# --- repeated from 02_hit_rate_at_k_in_code.py so this file runs on its own ---
def hit_rate_at_k(results, expected, k=5):
    # skip must-abstain cases
    pairs = [(g, e) for g, e
             in zip(results, expected) if e]
    hits = sum(1 for g, e in pairs
               if e & set(g[:k]))
    if not pairs:
        return float("nan")
    return hits / len(pairs)

# --- this slide ---
def recall_at_k(got, exp, k=5):
    if not exp:
        # score via abstention metrics instead
        return None
    found = exp & set(got[:k])
    return len(found) / len(exp)

got = ["d3", "d1", "d9"]
print(recall_at_k(got, {"d1", "d7"}, k=3))
print(hit_rate_at_k([got], [{"d1"}], k=3))
