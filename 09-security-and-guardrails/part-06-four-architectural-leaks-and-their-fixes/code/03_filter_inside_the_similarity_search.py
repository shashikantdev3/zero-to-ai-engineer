"""Zero to AI Engineer · Security and Guardrails · Part 6 of 11
Slide: Filter inside the similarity search
Run: python 03_filter_inside_the_similarity_search.py
"""
# Isolation is a mandatory filter
# on the similarity lookup.
def cached_answer(cache, vec, tenant, scope):
    hits = cache.search(
        vec,
        filter={"tenant_id": tenant,
                "scope_hash": scope},
        threshold=0.95,
        top_k=1,
    )
    return hits[0].answer if hits else None
