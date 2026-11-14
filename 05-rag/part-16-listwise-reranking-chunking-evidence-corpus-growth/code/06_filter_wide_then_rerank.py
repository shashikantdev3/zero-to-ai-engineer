"""Zero to AI Engineer · RAG and Vector Search · Part 16 of 26
Slide: Filter wide, then rerank
Run: python 06_filter_wide_then_rerank.py
"""
results = [
    ("leave policy v1", "hr", False, 0.91),
    ("leave policy v2", "hr", True, 0.89),
    ("sales leave tips", "sales", True, 0.90),
    ("leave form", "hr", True, 0.80),
]
# retrieve wide, filter to current hr docs
wide = [r for r in results
        if r[2] and r[1] == "hr"]
# then rerank and keep a few
top = sorted(wide, key=lambda r: -r[3])[:5]
print([r[0] for r in top])
