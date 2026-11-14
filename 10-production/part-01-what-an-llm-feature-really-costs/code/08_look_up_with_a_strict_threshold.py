"""Zero to AI Engineer · Production and LLMOps · Part 1 of 38
Slide: Look up with a strict threshold
Run: python 08_look_up_with_a_strict_threshold.py
"""
# --- repeated from 07_a_cache_key_per_tenant.py so this file runs on its own ---
def cache_key(tenant_id, scope_hash):
    # never shared across tenants
    return f"semcache:{tenant_id}:{scope_hash}"

# toy store: namespace -> cached entries
store = {cache_key("team_a", "s1"): [
    {"vec": (1.0, 0.0), "answer": "9 to 5",
     "personal": False, "expired": False}]}

# --- this slide ---
def lookup(q_vec, tenant, scope, th=0.95):
    ns = cache_key(tenant, scope)
    for e in store.get(ns, []):
        score = sum(a * b for a, b
                    in zip(q_vec, e["vec"]))
        if e["personal"] or e["expired"]:
            continue
        if score >= th:
            return e["answer"]
    return None
print(lookup((1.0, 0.0), "team_a", "s1"))
print(lookup((1.0, 0.0), "team_b", "s1"))
