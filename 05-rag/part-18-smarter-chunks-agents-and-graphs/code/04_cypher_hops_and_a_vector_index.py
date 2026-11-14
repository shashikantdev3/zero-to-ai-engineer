"""Zero to AI Engineer · RAG and Vector Search · Part 18 of 26
Slide: Cypher: hops and a vector index
Run: python 04_cypher_hops_and_a_vector_index.py
"""
HOPS = """
MATCH (s:Service {name: 'payments'})
  -[:DEPENDS_ON*1..3]->(d:Service)
RETURN DISTINCT d.name
"""
INDEX = """
CREATE VECTOR INDEX chunk_embedding
IF NOT EXISTS FOR (c:Chunk) ON c.embedding
OPTIONS {indexConfig: {
 `vector.dimensions`: 1536,
 `vector.similarity_function`: 'cosine'}}
"""
