"""Zero to AI Engineer · Evaluation · Part 7 of 11
Slide: Finding stale and orphaned docs
Run: python 04_finding_stale_and_orphaned_docs.py
"""
def stale_docs(source: dict, index: dict):
    # doc_id -> content hash or timestamp
    stale = [d for d, v in source.items()
             if index.get(d) != v]
    # deleted or renamed at source
    orphaned = [d for d in index
                if d not in source]
    return stale + orphaned
src = {"leave": "h2", "travel": "h1"}
idx = {"leave": "h1", "travel": "h1",
       "old-bonus": "h1"}
print(stale_docs(src, idx))
