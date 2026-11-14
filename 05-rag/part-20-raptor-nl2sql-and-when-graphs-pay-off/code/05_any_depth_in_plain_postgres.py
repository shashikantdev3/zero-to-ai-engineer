"""Zero to AI Engineer · RAG and Vector Search · Part 20 of 26
Slide: Any depth in plain Postgres
Run: python 05_any_depth_in_plain_postgres.py
"""
# Any-depth dependencies in plain Postgres
HEAD = "WITH RECURSIVE deps(name, path) AS ("
BASE = """
SELECT d.depends_on,
       ARRAY[d.service, d.depends_on]
FROM service_deps d
WHERE d.service = 'payments'
UNION ALL"""
