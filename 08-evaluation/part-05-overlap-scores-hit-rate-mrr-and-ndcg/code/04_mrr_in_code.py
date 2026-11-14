"""Zero to AI Engineer · Evaluation · Part 5 of 11
Slide: MRR in code
Run: python 04_mrr_in_code.py
"""
def mrr(results, expected):
    # skip must-abstain cases
    pairs = [(g, e) for g, e
             in zip(results, expected) if e]
    total = 0.0
    for got, exp in pairs:
        for rank, doc in enumerate(got, 1):
            if doc in exp:
                total += 1 / rank
                break
    n = len(pairs)
    return total / n if n else float("nan")
