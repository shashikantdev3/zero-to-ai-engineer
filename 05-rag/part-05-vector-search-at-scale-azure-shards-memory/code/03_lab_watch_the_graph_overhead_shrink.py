"""Zero to AI Engineer · RAG and Vector Search · Part 5 of 26
Follow-along lab: Watch the graph overhead shrink
Run: python 03_lab_watch_the_graph_overhead_shrink.py
"""
M = 16
for d in (128, 768, 1536):
    pct = 100 * (M * 2 * 4) / (d * 4)
    print(f"d={d}: graph adds {pct:.1f}%")
n = 10_000_000
vec_gb = n * 1536 * 4 / 1e9
graph_gb = n * M * 8 / 1e9
print(f"vectors {vec_gb:.2f} GB")
print(f"graph {graph_gb:.2f} GB")
print(f"pgvector ~{2 * vec_gb:.2f} GB")
