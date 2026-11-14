"""Zero to AI Engineer · RAG and Vector Search · Part 26 of 26
Slide: The MMR loop
Run: python 05_the_mmr_loop.py
"""
def mmr(q, docs, k=5, lam=0.7):
    # normalised vectors: dot is cosine
    rel = docs @ q
    sel, cand = [], list(range(len(docs)))
    while cand and len(sel) < k:
        red = redundancy(docs, cand, sel)
        gain = lam * rel[cand]
        scores = gain - (1 - lam) * red
        best = cand[int(np.argmax(scores))]
        sel.append(best)
        cand.remove(best)
    return sel
