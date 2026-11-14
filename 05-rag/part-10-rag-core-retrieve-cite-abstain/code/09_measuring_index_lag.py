"""Zero to AI Engineer · RAG and Vector Search · Part 10 of 26
Slide: Measuring index lag
Run: python 09_measuring_index_lag.py
"""
from datetime import datetime, timedelta
WINDOW = timedelta(hours=1)
monday = datetime(2026, 3, 2, 9)
sunday = datetime(2026, 3, 1, 9)
# doc id: (source_modified, indexed_at)
docs = {"leave": (monday, sunday),
        "travel": (sunday, monday)}
lag = max(mod - idx for mod, idx
          in docs.values())
print("index lag:", lag)
if lag > WINDOW:
    print("ALERT: index is stale")
