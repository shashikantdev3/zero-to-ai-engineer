"""Zero to AI Engineer · RAG and Vector Search · Part 7 of 26
Slide: Measure Both Stages
Run: python 04_measure_both_stages.py
"""
# --- repeated from 03_hit_rate_at_k.py so this file runs on its own ---
def hit_rate_at(results, relevant, k):
    # share of questions with a hit in top k
    hits = sum(
        any(r in rel for r in res[:k])
        for res, rel in zip(results, relevant)
    )
    return hits / len(results)

# --- this slide ---
gold = [{"d60"}, {"d2"}]
hybrid_ids = [
    [f"x{i}" for i in range(59)] + ["d60"],
    ["d2", "d7", "d9"]]
reranked_ids = [["x1", "x2"], ["d2", "d7"]]
# first stage: what the ranker can see
stage1 = hit_rate_at(hybrid_ids, gold, 50)
# after reranking: what the model sees
final = hit_rate_at(reranked_ids, gold, 5)
print(stage1, final)
