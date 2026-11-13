"""Zero to AI Engineer · Python · Part 25 of 25
Slide: Comparing tracemalloc snapshots
Run: python 05_comparing_tracemalloc_snapshots.py
"""
import tracemalloc

tracemalloc.start()
before = tracemalloc.take_snapshot()
LEAK = []
for i in range(100_000):
    # stands in for an unbounded cache
    LEAK.append(f"request-{i}")
after = tracemalloc.take_snapshot()
diff = after.compare_to(before, "lineno")
for stat in diff[:3]:
    print(stat)
