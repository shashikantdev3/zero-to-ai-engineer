"""Zero to AI Engineer · RAG and Vector Search · Part 19 of 26
Slide: Resolving the User's Groups
Run: python 02_resolving_the_users_groups.py
"""
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
