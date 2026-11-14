"""Zero to AI Engineer · Security and Guardrails · Part 6 of 11
Slide: Exact-match keys carry the tenant
Run: python 04_exact_match_keys_carry_the_tenant.py
"""
import hashlib
# Exact-match cache: key carries
# tenant and permission scope.
def cache_key(tenant, scope, query):
    raw = f"{tenant}|{scope}|{query}"
    digest = hashlib.sha256(raw.encode())
    return digest.hexdigest()
a = cache_key("tenant-a", "s1", "refund")
b = cache_key("tenant-b", "s1", "refund")
print(a == b)
