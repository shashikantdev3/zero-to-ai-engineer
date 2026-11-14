"""Zero to AI Engineer · RAG and Vector Search · Part 24 of 26
Slide: A Per-Segment Report in Pandas
Run: python 01_a_per_segment_report_in_pandas.py
"""
# Needs: pip install pandas
import pandas as pd
results = [
    {"segment": "hr", "hit": 1, "rr": 1.0},
    {"segment": "hr", "hit": 1, "rr": 0.5},
    {"segment": "legal", "hit": 0, "rr": 0.0},
]
df = pd.DataFrame(results)
report = df.groupby("segment").agg(
    cases=("hit", "size"),
    hit_rate=("hit", "mean"),
    mrr=("rr", "mean"))
print(report.sort_values("hit_rate"))
