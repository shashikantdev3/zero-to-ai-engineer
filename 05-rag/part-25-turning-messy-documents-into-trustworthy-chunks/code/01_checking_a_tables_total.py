"""Zero to AI Engineer · RAG and Vector Search · Part 25 of 26
Slide: Checking a table's total
Run: python 01_checking_a_tables_total.py
"""
def total_matches(rows, col, total, tol=0.01):
    s = sum(float(r[col]) for r in rows)
    return abs(s - total) <= tol

rows = [
    {"grade": "4", "days": "18"},
    {"grade": "5", "days": "20"},
]
print(total_matches(rows, "days", 38))
print(total_matches(rows, "days", 40))
