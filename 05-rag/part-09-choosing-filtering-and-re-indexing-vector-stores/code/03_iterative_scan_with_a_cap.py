"""Zero to AI Engineer · RAG and Vector Search · Part 9 of 26
Slide: Iterative scan with a cap
Run: python 03_iterative_scan_with_a_cap.py
"""
# iterative scan: keep pulling candidates
LIMIT, CAP = 10, 400
rows, scanned = [], 0
while len(rows) < LIMIT and scanned < CAP:
    # every 14th candidate is tenant t1
    if scanned % 14 == 0:
        rows.append(scanned)
    scanned += 1
print(len(rows), "rows,", scanned, "scanned")
