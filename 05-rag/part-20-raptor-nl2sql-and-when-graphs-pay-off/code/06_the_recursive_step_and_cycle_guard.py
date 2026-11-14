"""Zero to AI Engineer · RAG and Vector Search · Part 20 of 26
Slide: The recursive step and cycle guard
Run: python 06_the_recursive_step_and_cycle_guard.py
"""
# --- repeated from 05_any_depth_in_plain_postgres.py so this file runs on its own ---
# Any-depth dependencies in plain Postgres
HEAD = "WITH RECURSIVE deps(name, path) AS ("
BASE = """
SELECT d.depends_on,
       ARRAY[d.service, d.depends_on]
FROM service_deps d
WHERE d.service = 'payments'
UNION ALL"""

# --- this slide ---
STEP = """
SELECT d.depends_on, deps.path || d.depends_on
FROM service_deps d JOIN deps
  ON d.service = deps.name
WHERE NOT d.depends_on = ANY(deps.path))
SELECT DISTINCT name FROM deps;"""
QUERY = HEAD + BASE + STEP
print(QUERY)
