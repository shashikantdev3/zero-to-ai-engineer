"""Zero to AI Engineer · LLM Fundamentals · Part 14 of 18
Slide: A Top-k Filter
Run: python 04_a_top_k_filter.py
"""
def top_k_filter(probs, k):
    # positions sorted by probability
    order = sorted(range(len(probs)),
                   key=lambda i: probs[i])
    keep = order[-k:]
    out = [0.0] * len(probs)
    for i in keep:
        out[i] = probs[i]
    total = sum(out)
    return [x / total for x in out]

print(top_k_filter([0.5, 0.3, 0.2], 2))
