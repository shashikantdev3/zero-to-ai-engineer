"""Zero to AI Engineer · Evaluation · Part 5 of 11
Slide: NDCG at k in code
Run: python 06_ndcg_at_k_in_code.py
"""
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
