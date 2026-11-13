"""Zero to AI Engineer · Python · Part 16 of 25
Slide: Top k with heapq, buckets with bisect
Run: python 03_top_k_with_heapq_buckets_with_bisect.py
"""
import heapq, bisect
def top_k(scores: list, k: int) -> list:
    heap: list = []
    for s in scores:
        if len(heap) < k:
            heapq.heappush(heap, s)
        elif s > heap[0]:
            heapq.heapreplace(heap, s)
    return sorted(heap, reverse=True)
edges = [0, 100, 500, 1000]
# 1, the 100 to 499 bucket
bucket = bisect.bisect_right(edges, 250) - 1
