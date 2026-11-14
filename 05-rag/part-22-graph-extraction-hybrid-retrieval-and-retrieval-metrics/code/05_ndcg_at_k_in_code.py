"""Zero to AI Engineer · RAG and Vector Search · Part 22 of 26
Slide: NDCG at k in code
Run: python 05_ndcg_at_k_in_code.py
"""
import math
def ndcg_at_k(res, rel, k=10):
    # binary relevance, one query
    dcg = sum(
        1 / math.log2(i + 1)
        for i, r in enumerate(res[:k], 1)
        if r in rel)
    n = min(len(rel), k)
    ideal = sum(1 / math.log2(i + 1)
                for i in range(1, n + 1))
    return dcg / ideal if ideal else 0.0
print(ndcg_at_k(["a", "b"], {"b"}))
