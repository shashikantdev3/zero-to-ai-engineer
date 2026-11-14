"""Zero to AI Engineer · RAG and Vector Search · Part 15 of 26
Slide: Compare variants on a golden set
Run: python 08_compare_variants_on_a_golden_set.py
"""
# --- repeated from 07_two_retrieval_metrics.py so this file runs on its own ---
def mrr(runs, gold):
    total = 0.0
    for ids, rel in zip(runs, gold):
        for i, d in enumerate(ids, 1):
            if d in rel:
                total += 1 / i
                break
    return total / len(runs)
def hit_rate(runs, gold, k):
    hits = [bool(set(ids[:k]) & rel)
            for ids, rel in zip(runs, gold)]
    return sum(hits) / len(runs)

# --- this slide ---
gold = [{"d2"}, {"d7"}]
runs = {
    "vector": [["d1", "d2"], ["d3", "d4"]],
    "hybrid": [["d2", "d1"], ["d4", "d7"]],
    "hybrid+rerank": [["d2", "d1"],
                      ["d7", "d4"]],
}
for name, ids in runs.items():
    print(name, "MRR", mrr(ids, gold),
          "hit@5", hit_rate(ids, gold, 5))
