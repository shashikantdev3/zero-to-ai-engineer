"""Zero to AI Engineer · RAG and Vector Search · Part 21 of 26
Slide: Idempotent load with MERGE
Run: python 01_idempotent_load_with_merge.py
"""
# Idempotent load: merge each node first
LOAD = """
MERGE (s:Service {name: $service})
MERGE (t:Team {name: $team})
MERGE (s)-[:OWNED_BY]->(t)
"""
params = {"service": "checkout",
          "team": "payments"}
print(LOAD.strip())
print(params)
