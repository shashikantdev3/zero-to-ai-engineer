"""Zero to AI Engineer · Security and Guardrails · Part 6 of 11
Slide: Three tokens, three paths
Run: python 02_three_tokens_three_paths.py
"""
# --- repeated from 01_reading_groups_safely.py so this file runs on its own ---
def user_groups(claims, graph):
    if "groups" in claims:
        return claims["groups"]
    names = claims.get("_claim_names", {})
    over = "groups" in names
    if over or claims.get("hasgroups"):
        # Skip _claim_sources; call Graph.
        oid = claims["oid"]
        return graph.get_member_groups(oid)
    # default deny
    return []

# --- this slide ---
class FakeGraph:
    def get_member_groups(self, oid):
        return ["a1b2-object-id"]
g = FakeGraph()
small = {"groups": ["9f3c-object-id"]}
big = {"_claim_names": {"groups": "src1"},
       "oid": "user-oid-1"}
print(user_groups(small, g))
print(user_groups(big, g))
print(user_groups({}, g))
