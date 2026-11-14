"""Zero to AI Engineer · RAG and Vector Search · Part 17 of 26
Slide: Running the phrasings in parallel
Run: python 04_running_the_phrasings_in_parallel.py
"""
# --- repeated from 03_fusion_and_a_stand_in_search.py so this file runs on its own ---
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

# --- this slide ---
def generate_variants(q, n=3):
    # real system: one small model call
    return [f"{q} v{i}" for i in range(n)]

async def multi_query(q0):
    qs = [q0] + generate_variants(q0, n=3)
    res = await asyncio.gather(
        *(search_async(q, k=30) for q in qs))
    return rrf(res)
fused = asyncio.run(multi_query(
    "Can contractors take parental leave?"))
print(fused)
