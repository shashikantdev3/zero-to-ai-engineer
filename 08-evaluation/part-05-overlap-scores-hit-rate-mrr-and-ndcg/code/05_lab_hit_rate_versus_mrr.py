"""Zero to AI Engineer · Evaluation · Part 5 of 11
Follow-along lab: Hit rate versus MRR
Run: python 05_lab_hit_rate_versus_mrr.py
"""
exp = ["d1", "d3"]
before = [["d4","d2","d1"], ["d5","d3","d6"]]
after = [["d1","d4","d2"], ["d3","d5","d6"]]
n = len(exp)
def report(name, runs):
    ranks = [r.index(e) + 1
             for r, e in zip(runs, exp)]
    hit = sum(1 for x in ranks if x <= 3)
    mrr = sum(1 / x for x in ranks) / n
    print(name, "hit@3:", hit / n)
    print(name, "MRR:", round(mrr, 2))
report("before", before)
report("after", after)
