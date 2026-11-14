"""Zero to AI Engineer · RAG and Vector Search · Part 19 of 26
Slide: Building the Deny-by-Default Filter
Run: python 03_building_the_deny_by_default_filter.py
"""
# --- repeated from 02_resolving_the_users_groups.py so this file runs on its own ---
import re
GUID = re.compile(
    r"^[0-9a-f]{8}(-[0-9a-f]{4}){3}"
    r"-[0-9a-f]{12}$", re.I)
def resolve_groups(claims, lookup):
    ids = []
    names = claims.get("_claim_names", {})
    if "groups" in claims:
        ids = claims["groups"]
    elif "groups" in names:
        ids = lookup(claims["oid"])
    return [g for g in ids if GUID.match(g)]

# --- this slide ---
def permission_filter(groups):
    if not groups:
        # default deny: never search unfiltered
        raise PermissionError("no groups: deny")
    joined = ",".join(groups)
    return ("group_ids/any(g: search.in("
            f"g, '{joined}', ','))")

claims = {"groups": [
    "11111111-2222-3333-4444-555555555555"]}
ids = resolve_groups(claims, lambda oid: [])
print(permission_filter(ids))
