"""Zero to AI Engineer · Evaluation · Part 7 of 11
Follow-along lab: Hash, compare, label
Run: python 05_lab_hash_compare_label.py
"""
import hashlib
def h(text):
    return hashlib.md5(text.encode()).digest()
src = {"leave": h("20 days"),
       "travel": h("economy")}
idx = {"leave": h("18 days"),
       "travel": h("economy"),
       "old-bonus": h("10 percent")}
for d in sorted(src | idx):
    if d not in src:
        print(d, "-> orphaned, still indexed")
    elif idx[d] != src[d]:
        print(d, "-> stale, re-index")
    else: print(d, "-> fresh")
