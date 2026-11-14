"""Zero to AI Engineer · RAG and Vector Search · Part 21 of 26
Slide: Vector search, then traverse
Run: python 05_vector_search_then_traverse.py
"""
# Procedure form: check your Neo4j version
SEARCH = """
CALL db.index.vector.queryNodes(
  'chunk_embedding', 5, $queryVector)
YIELD node AS chunk, score
MATCH (chunk)-[:MENTIONS]->(e)
RETURN chunk.text, score,
  collect(DISTINCT e.name) AS entities
"""
print(SEARCH.strip())
