"""Zero to AI Engineer · RAG and Vector Search · Part 6 of 26
Follow-along lab: Planning lists and probes
Run: python 03_lab_planning_lists_and_probes.py
"""
import math

def ivf_plan(rows):
    if rows <= 1_000_000:
        lists = rows // 1000
    else:
        lists = math.isqrt(rows)
    return lists, round(math.sqrt(lists))
for rows in (100_000, 1_000_000, 4_000_000):
    lists, probes = ivf_plan(rows)
    msg = f"lists={lists} probes={probes}"
    print(f"{rows:>9} rows: {msg}")
share = 1 / 1000
print(f"probes=1 of 1000 lists: {share:.1%}")
