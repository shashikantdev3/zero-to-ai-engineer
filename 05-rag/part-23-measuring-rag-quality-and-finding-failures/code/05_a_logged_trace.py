"""Zero to AI Engineer · RAG and Vector Search · Part 23 of 26
Slide: A logged trace
Run: python 05_a_logged_trace.py
"""
from types import SimpleNamespace

def has(ids, rel):
    return any(i in ids for i in rel)

trace = SimpleNamespace(
    index_ids=["c1", "c2", "c7"],
    retrieved_ids=["c3", "c4", "c5", "c6",
                   "c2", "c7"],
    cited_ids=["c3"],
)
