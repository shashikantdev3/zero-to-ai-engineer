"""Zero to AI Engineer · Prompting · Part 6 of 10
Slide: Compact at a threshold
Run: python 05_compact_at_a_threshold.py
"""
def compact(system, h, keep=6, limit=6000):
    if n_tokens(render(h)) < limit:
        return system, h
    cut = safe_cut(h, keep)
    if cut == 0:
        # no safe cut: trim tool outputs
        return system, h
    summary = llm(SUMMARISE, render(h[:cut]))
    note = {"role": "user",
            "content": fence(summary)}
    # system message stays unchanged
    return system, [note] + h[cut:]
