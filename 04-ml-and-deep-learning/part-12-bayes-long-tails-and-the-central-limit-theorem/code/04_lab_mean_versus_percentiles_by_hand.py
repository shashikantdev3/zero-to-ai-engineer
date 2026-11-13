"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 12 of 28
Follow-along lab: Mean versus percentiles, by hand
Run: python 04_lab_mean_versus_percentiles_by_hand.py
"""
import random
import statistics as st

rng = random.Random(0)
lat = [rng.lognormvariate(3.9, 0.8)
       for _ in range(50_000)]
cuts = st.quantiles(lat, n=100)
m, sd = st.fmean(lat), st.stdev(lat)
print(f"median   {cuts[49]:7.1f} ms")
print(f"mean     {m:7.1f} ms")
print(f"p95      {cuts[94]:7.1f} ms")
print(f"p99      {cuts[98]:7.1f} ms")
print(f"mean+2sd {m + 2 * sd:7.1f} ms")
