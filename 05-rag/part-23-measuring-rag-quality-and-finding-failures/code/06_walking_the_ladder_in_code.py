"""Zero to AI Engineer · RAG and Vector Search · Part 23 of 26
Slide: Walking the ladder in code
Run: python 06_walking_the_ladder_in_code.py
"""
# --- repeated from 05_a_logged_trace.py so this file runs on its own ---
from types import SimpleNamespace

def has(ids, rel):
    return any(i in ids for i in rel)

trace = SimpleNamespace(
    index_ids=["c1", "c2", "c7"],
    retrieved_ids=["c3", "c4", "c5", "c6",
                   "c2", "c7"],
    cited_ids=["c3"],
)

# --- this slide ---
def diagnose(t, rel, k_sent=5):
    if not has(t.index_ids, rel):
        return "not in index: ingestion, sync"
    if not has(t.retrieved_ids, rel):
        return "not retrieved: query, filter"
    if not has(t.retrieved_ids[:k_sent], rel):
        return "below cut: reranker or k"
    if not has(t.cited_ids, rel):
        return "sent but unused: prompt"
    return "model or reference issue"

print(diagnose(trace, ["c7"]))
