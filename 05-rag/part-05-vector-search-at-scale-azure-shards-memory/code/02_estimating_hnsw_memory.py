"""Zero to AI Engineer · RAG and Vector Search · Part 5 of 26
Slide: Estimating HNSW memory
Run: python 02_estimating_hnsw_memory.py
"""
def hnsw_memory_gb(n, d, m=16, bpd=4):
    vectors = n * d * bpd
    # FAISS: about 2*M links of 4 bytes
    graph = n * m * 2 * 4
    v_gb = round(vectors / 1e9, 2)
    g_gb = round(graph / 1e9, 2)
    return v_gb, g_gb

print(hnsw_memory_gb(10_000_000, 1536))
print(hnsw_memory_gb(10_000_000, 128))
# pgvector: table copy plus index copy,
# so budget about 2 x 61.44 GB of vectors
