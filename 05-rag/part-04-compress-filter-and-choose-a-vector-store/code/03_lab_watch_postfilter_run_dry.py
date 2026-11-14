"""Zero to AI Engineer · RAG and Vector Search · Part 4 of 26
Follow-along lab: Watch postfilter run dry
Run: python 03_lab_watch_postfilter_run_dry.py
"""
import random
random.seed(7)
N, k = 1000, 10
sc = [random.random() for _ in range(N)]
order = sorted(range(N), key=lambda i: sc[i])
# filter: only 1 percent of docs are HR
hr = set(range(0, N, 100))
post = [i for i in order[:k] if i in hr]
wide = [i for i in order[:100] if i in hr]
pre = [i for i in order if i in hr][:k]
print("eligible docs:", len(hr))
print("postfilter, k=10:", len(post))
print("postfilter, k=100:", len(wide))
print("prefilter, k=10:", len(pre))
