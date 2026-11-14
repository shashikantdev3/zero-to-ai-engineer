"""Zero to AI Engineer · RAG and Vector Search · Part 4 of 26
Slide: The table and its index
Run: python 04_the_table_and_its_index.py
"""
schema = """
CREATE EXTENSION IF NOT EXISTS vector;
CREATE TABLE chunks (
  id bigserial PRIMARY KEY,
  tenant_id text NOT NULL,
  body text NOT NULL,
  embedding vector(1536)
);
CREATE INDEX ON chunks USING hnsw
  (embedding vector_cosine_ops)
  WITH (m = 16, ef_construction = 64);
"""
