"""Zero to AI Engineer · RAG and Vector Search · Part 6 of 26
Slide: A partial index per tenant
Run: python 05_a_partial_index_per_tenant.py
"""
# Few distinct values: one graph per value
for t in ["t1", "t2", "t3"]:
    sql = (
        f"CREATE INDEX chunks_{t}_hnsw"
        " ON chunks USING hnsw"
        " (embedding vector_cosine_ops)"
        f" WHERE tenant_id = '{t}';"
    )
    print(sql)
