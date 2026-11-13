"""Zero to AI Engineer · LLM Fundamentals · Part 14 of 18
Slide: A Top-p Filter
Run: python 05_a_top_p_filter.py
"""
def top_p_filter(probs, p=0.9):
    order = sorted(range(len(probs)),
                   key=lambda i: -probs[i])
    keep, total = [], 0.0
    for i in order:
        keep.append(i)
        total += probs[i]
        if total >= p:
            break
    out = [probs[i] if i in keep else 0.0
           for i in range(len(probs))]
    return [x / sum(out) for x in out]
