"""Zero to AI Engineer · Evaluation · Part 6 of 11
Follow-along lab: Move good chunks, watch the score
Run: python 02_lab_move_good_chunks_watch_the_score.py
"""
def cp_at_k(flags, k):
    score, hits = 0.0, 0
    for i, r in enumerate(flags[:k], 1):
        if r:
            hits += 1
            score += hits / i
    return score / hits if hits else 0.0

top = [True, True, False, False]
low = [False, False, True, True]
none = [False] * 4
for name, f in [("top", top), ("bottom", low),
                ("none", none)]:
    print(name, round(cp_at_k(f, 4), 2))
