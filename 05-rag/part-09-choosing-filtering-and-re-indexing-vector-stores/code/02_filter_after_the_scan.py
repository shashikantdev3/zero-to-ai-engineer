"""Zero to AI Engineer · RAG and Vector Search · Part 9 of 26
Slide: Filter after the scan
Run: python 02_filter_after_the_scan.py
"""
# 40 nearest candidates: (id, tenant)
cands = [(i, "t1" if i % 14 == 0 else "t2")
         for i in range(40)]
LIMIT = 10
# the filter runs AFTER the index scan
hits = [c for c in cands if c[1] == "t1"]
print(len(hits[:LIMIT]), "rows, not", LIMIT)
