"""Zero to AI Engineer · Production and LLMOps · Part 9 of 38
Follow-along lab: Count the token buckets
Run: python 03_lab_count_the_token_buckets.py
"""
pods, workers = 3, 4
buckets = {}
for p in range(pods):
    for w in range(workers):
        # each process has its own memory
        buckets[(p, w)] = 10
print("buckets:", len(buckets))
limit = buckets[(0, 0)]
print("limit per bucket:", limit)
total = limit * len(buckets)
print("real cluster limit:", total)
print("intended limit:", limit)
