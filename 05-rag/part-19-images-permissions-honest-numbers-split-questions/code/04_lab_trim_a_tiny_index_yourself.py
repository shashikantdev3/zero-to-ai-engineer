"""Zero to AI Engineer · RAG and Vector Search · Part 19 of 26
Follow-along lab: Trim a Tiny Index Yourself
Run: python 04_lab_trim_a_tiny_index_yourself.py
"""
acl = {"hr1": ["hr"], "pub": ["all"],
       "canary": ["legal"], "orphan": []}
def search(groups):
    if not groups:
        return "denied: no groups"
    return [d for d, allowed in acl.items()
            if set(allowed) & set(groups)]
print("hr user:", search(["hr", "all"]))
print("legal:", search(["legal"]))
print("no groups:", search([]))
print("canary seen by hr:",
      "canary" in search(["hr", "all"]))
