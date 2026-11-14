"""Zero to AI Engineer · Security and Guardrails · Part 5 of 11
Slide: A server-built security filter
Run: python 08_a_server_built_security_filter.py
"""
# Groups come from a trusted source:
# the user's verified identity
groups = ["grp-0001", "grp-0002"]
ids = ",".join(groups)
body = {
    "search": "parental leave",
    "filter": "group_ids/any(g: search.in("
              f"g, '{ids}', ','))",
    "top": 10,
}
print(body["filter"])
