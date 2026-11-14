"""Zero to AI Engineer · RAG and Vector Search · Part 21 of 26
Slide: Constraint and vector index
Run: python 04_constraint_and_vector_index.py
"""
CONSTRAINT = """
CREATE CONSTRAINT service_name IF NOT EXISTS
FOR (s:Service) REQUIRE s.name IS UNIQUE
"""
INDEX = """
CREATE VECTOR INDEX chunk_embedding
IF NOT EXISTS
FOR (c:Chunk) ON c.embedding
OPTIONS {indexConfig: {
  `vector.dimensions`: 1536,
  `vector.similarity_function`: 'cosine'}}
"""
