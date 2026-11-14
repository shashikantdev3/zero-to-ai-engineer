"""Zero to AI Engineer · RAG and Vector Search · Part 9 of 26
Follow-along lab: Estimate HNSW memory
Run: python 01_lab_estimate_hnsw_memory.py
"""
n, dim, m = 10_000_000, 1536, 16
# float32 means 4 bytes per number
vec = n * dim * 4
# graph: about 2 * M links, 4 bytes each
graph = n * 2 * m * 4
total = vec + graph
print(f"vectors: {vec / 1e9:.1f} GB")
print(f"graph: {graph / 1e9:.1f} GB")
print(f"total: {total / 1e9:.1f} GB")
share = graph / total * 100
print(f"graph share: {share:.0f} percent")
print(f"pgvector: {2 * vec / 1e9:.0f} GB")
