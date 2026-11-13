"""Zero to AI Engineer · Python · Part 16 of 25
Follow-along lab: Containers in five prints
Run: python 04_lab_containers_in_five_prints.py
"""
import heapq, bisect
from collections import Counter, deque
codes = ["429", "500", "429", "503"]
print(Counter(codes).most_common(1))
window = deque([120, 80, 95, 300], maxlen=3)
print(list(window))
heap: list[int] = []
for x in [5, 1, 8]:
    heapq.heappush(heap, x)
print(heap[0])
print(heapq.nlargest(2, [0.2, 0.9, 0.5]))
edges = [0, 100, 500, 1000]
print(bisect.bisect_right(edges, 250) - 1)
