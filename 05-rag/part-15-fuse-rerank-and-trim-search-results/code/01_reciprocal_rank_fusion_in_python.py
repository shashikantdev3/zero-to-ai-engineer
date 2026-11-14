"""Zero to AI Engineer · RAG and Vector Search · Part 15 of 26
Slide: Reciprocal rank fusion in Python
Run: python 01_reciprocal_rank_fusion_in_python.py
"""
def rrf(rankings, k=60):
    scores = {}
    for r in rankings:
        for rank, d in enumerate(r, 1):
            old = scores.get(d, 0.0)
            scores[d] = old + 1.0 / (k + rank)
    return sorted(scores, key=scores.get,
                  reverse=True)

bm25_ids = ["a", "b", "c"]
vector_ids = ["c", "a", "d"]
fused = rrf([bm25_ids, vector_ids])
