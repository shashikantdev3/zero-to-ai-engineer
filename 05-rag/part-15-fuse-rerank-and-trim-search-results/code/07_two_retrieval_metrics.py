"""Zero to AI Engineer · RAG and Vector Search · Part 15 of 26
Slide: Two retrieval metrics
Run: python 07_two_retrieval_metrics.py
"""
def mrr(runs, gold):
    total = 0.0
    for ids, rel in zip(runs, gold):
        for i, d in enumerate(ids, 1):
            if d in rel:
                total += 1 / i
                break
    return total / len(runs)
def hit_rate(runs, gold, k):
    hits = [bool(set(ids[:k]) & rel)
            for ids, rel in zip(runs, gold)]
    return sum(hits) / len(runs)
