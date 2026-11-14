"""Zero to AI Engineer · RAG and Vector Search · Part 22 of 26
Slide: Hit rate and MRR in code
Run: python 04_hit_rate_and_mrr_in_code.py
"""
def hit_rate(results, relevant, k=5):
    pairs = zip(results, relevant)
    hits = sum(any(r in rel for r in res[:k])
               for res, rel in pairs)
    return hits / len(results)
def mrr(results, relevant):
    total = 0.0
    for res, rel in zip(results, relevant):
        ranks = enumerate(res, 1)
        total += next((1 / i for i, r in ranks
                       if r in rel), 0.0)
    return total / len(results)
