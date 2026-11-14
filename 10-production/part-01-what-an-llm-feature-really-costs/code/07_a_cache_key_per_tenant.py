"""Zero to AI Engineer · Production and LLMOps · Part 1 of 38
Slide: A cache key per tenant
Run: python 07_a_cache_key_per_tenant.py
"""
def cache_key(tenant_id, scope_hash):
    # never shared across tenants
    return f"semcache:{tenant_id}:{scope_hash}"

# toy store: namespace -> cached entries
store = {cache_key("team_a", "s1"): [
    {"vec": (1.0, 0.0), "answer": "9 to 5",
     "personal": False, "expired": False}]}
