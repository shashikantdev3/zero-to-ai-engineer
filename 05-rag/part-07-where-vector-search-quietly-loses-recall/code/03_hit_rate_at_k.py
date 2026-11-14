"""Zero to AI Engineer · RAG and Vector Search · Part 7 of 26
Slide: Hit Rate at K
Run: python 03_hit_rate_at_k.py
"""
def hit_rate_at(results, relevant, k):
    # share of questions with a hit in top k
    hits = sum(
        any(r in rel for r in res[:k])
        for res, rel in zip(results, relevant)
    )
    return hits / len(results)
