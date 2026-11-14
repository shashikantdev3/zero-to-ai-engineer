"""Zero to AI Engineer · RAG and Vector Search · Part 8 of 26
Slide: pg_diskann in Azure PostgreSQL
Run: python 01_pg_diskann_in_azure_postgresql.py
"""
# Azure Database for PostgreSQL
# check the current Azure docs for syntax
setup = (
    "CREATE EXTENSION IF NOT EXISTS "
    "pg_diskann CASCADE;"
)
index = (
    "CREATE INDEX ON chunks USING diskann "
    "(embedding vector_cosine_ops);"
)
print(setup)
print(index)
