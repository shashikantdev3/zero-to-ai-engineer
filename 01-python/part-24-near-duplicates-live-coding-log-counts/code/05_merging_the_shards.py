"""Zero to AI Engineer · Python · Part 24 of 25
Slide: Merging the shards
Run: python 05_merging_the_shards.py
"""
from collections import Counter

def merge(shards: list[Counter]) -> Counter:
    total: Counter = Counter()
    for c in shards:
        # reduce step
        total.update(c)
    return total

# count_emails("audit.log").most_common(10)
