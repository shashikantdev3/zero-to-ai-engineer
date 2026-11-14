"""Zero to AI Engineer · Evaluation · Part 5 of 11
Slide: Two NDCG cases
Run: python 07_two_ndcg_cases.py
"""
# --- repeated from 06_ndcg_at_k_in_code.py so this file runs on its own ---
import math
def ndcg_at_k(got_rels, all_rels, k=10):
    # got_rels: grades in rank order
    # all_rels: ALL judged docs, even missed
    def dcg(rels):
        top = rels[:k]
        return sum(r / math.log2(i + 2)
            for i, r in enumerate(top))
    best = sorted(all_rels, reverse=True)
    ideal = dcg(best)
    return (dcg(got_rels) / ideal
            if ideal > 0 else 0.0)

# --- this slide ---
# continues the ndcg_at_k slide
# right chunk at rank 2
print(ndcg_at_k([0, 2, 1], [2, 1]))
# missed relevant docs lower it too
print(ndcg_at_k([2, 0, 0], [2, 2, 1]))
