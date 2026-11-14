"""Zero to AI Engineer · RAG and Vector Search · Part 8 of 26
Slide: Compare at equal recall
Run: python 06_compare_at_equal_recall.py
"""
def fair_compare(configs, xb, queries):
    exact = exact_top_k(xb, queries, K)
    for name, search, knobs in configs:
        for knob in knobs:
            res = [search(q, K, knob)
                   for q in queries]
            ids, lat = zip(*res)
            rec = recall_at_k(ids, exact, K)
            if rec >= TARGET:
                p95 = np.percentile(lat, 95)
                print(name, knob, rec, p95)
                break
