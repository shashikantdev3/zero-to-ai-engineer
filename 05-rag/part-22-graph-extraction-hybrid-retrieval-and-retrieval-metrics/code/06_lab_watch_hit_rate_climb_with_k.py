"""Zero to AI Engineer · RAG and Vector Search · Part 22 of 26
Follow-along lab: Watch hit rate climb with k
Run: python 06_lab_watch_hit_rate_climb_with_k.py
"""
runs = [["a", "x", "b"], ["y", "c", "z"],
        ["p", "q", "r"]]
gold = [{"a"}, {"c"}, {"r"}]
pairs = list(zip(runs, gold))
for k in (1, 2, 3):
    hits = sum(any(d in g for d in r[:k])
               for r, g in pairs)
    print(f"hit rate@{k}: {hits / 3:.2f}")
def first(r, g):
    ranks = enumerate(r, 1)
    return next((1 / i for i, d in ranks
                 if d in g), 0.0)
mrr = sum(first(r, g) for r, g in pairs) / 3
print(f"MRR: {mrr:.2f}")
