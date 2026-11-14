"""Zero to AI Engineer · RAG and Vector Search · Part 17 of 26
Slide: Fusion and a stand-in search
Run: python 03_fusion_and_a_stand_in_search.py
"""
import asyncio
def rrf(lists, k=60):
    scores = {}
    for ranked in lists:
        for rank, doc in enumerate(ranked, 1):
            s = scores.get(doc, 0)
            scores[doc] = s + 1 / (k + rank)
    return sorted(scores, key=scores.get,
                  reverse=True)
async def search_async(q, k=30):
    await asyncio.sleep(0.1)
    return [f"doc-{len(q) % 5}", "doc-9"][:k]
