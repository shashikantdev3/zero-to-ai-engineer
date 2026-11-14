"""Zero to AI Engineer · Security and Guardrails · Part 6 of 11
Slide: Reading groups safely
Run: python 01_reading_groups_safely.py
"""
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
