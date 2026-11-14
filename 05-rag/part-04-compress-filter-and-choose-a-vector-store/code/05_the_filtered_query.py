"""Zero to AI Engineer · RAG and Vector Search · Part 4 of 26
Slide: The filtered query
Run: python 05_the_filtered_query.py
"""
query = """
SET hnsw.ef_search = 100;
-- 0.8.0+, off by default
SET hnsw.iterative_scan = strict_order;
SELECT id, body
FROM chunks
WHERE tenant_id = 'tenant_a'
ORDER BY embedding <=> $1
LIMIT 10;
"""
print(query.strip())
