"""Zero to AI Engineer · RAG and Vector Search · Part 5 of 26
Slide: A hybrid plus semantic query
Run: python 01_a_hybrid_plus_semantic_query.py
"""
import json
q = "parental leave carry forward"
body = {"search": q, "top": 5,
  "vectorQueries": [{"kind": "text",
    "text": q, "fields": "contentVector",
    "k": 50}],
  "filter": "group_ids/any(g: search.in("
            "g, 'grp-hr,grp-all'))",
  "queryType": "semantic",
  "semanticConfiguration": "default"}
print(json.dumps(body, indent=2))
