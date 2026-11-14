"""Zero to AI Engineer · RAG and Vector Search · Part 6 of 26
Slide: M and ef_search in pgvector
Run: python 01_m_and_ef_search_in_pgvector.py
"""
# pgvector HNSW: M and efConstruction at build
build = (
    "CREATE INDEX ON chunks USING hnsw "
    "(embedding vector_cosine_ops) "
    "WITH (m = 32, ef_construction = 128);"
)
# efSearch at query time; must be >= LIMIT k
ef_search, k = 100, 10
assert ef_search >= k
query = f"SET hnsw.ef_search = {ef_search};"
print(build)
print(query)
