"""Zero to AI Engineer · RAG and Vector Search · Part 21 of 26
Slide: Bounded multi-hop query
Run: python 02_bounded_multi_hop_query.py
"""
# Bounded multi-hop: up to 3 hops
QUERY = """
MATCH (:Service {name: 'checkout'})
  -[:DEPENDS_ON*1..3]->(d:Service)
  -[:OWNED_BY]->(t:Team)
RETURN t.name AS team,
  count(DISTINCT d) AS dependencies
ORDER BY dependencies DESC
"""
print(QUERY.strip())
