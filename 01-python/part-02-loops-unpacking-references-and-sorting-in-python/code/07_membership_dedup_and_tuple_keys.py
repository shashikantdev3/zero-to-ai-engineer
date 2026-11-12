"""Zero to AI Engineer · Python · Part 2 of 25
Slide: Membership, Dedup and Tuple Keys
Run: python 07_membership_dedup_and_tuple_keys.py
"""
seen_ids = ["d1", "d2", "d3"]
# O(n) per "in" on the list
seen = set(seen_ids)
# O(1) average per "in" on the set
candidates = ["d2", "d4", "d5"]
fresh = [c for c in candidates
         if c not in seen]
# tuple as a dict key
cache = {("tenant-a", "q1"): "answer"}
print(fresh)
