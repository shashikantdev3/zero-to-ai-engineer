"""Zero to AI Engineer · RAG and Vector Search · Part 11 of 26
Follow-along lab: Watch Stale Chunks Survive
Run: python 03_lab_watch_stale_chunks_survive.py
"""
index = {}
def put(doc, n, ver):
    ids = {f"{doc}-{i}" for i in range(n)}
    for i in ids:
        index[i] = ver
    return ids
put("policy", 12, "v1")
print("after v1:", len(index))
new = put("policy", 9, "v2")
print("upsert only:", len(index))
stale = set(index) - new
print("stale left:", len(stale))
for k in stale: del index[k]
print("after delete:", len(index))
