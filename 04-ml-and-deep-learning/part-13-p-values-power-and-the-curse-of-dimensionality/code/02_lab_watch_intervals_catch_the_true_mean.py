"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 13 of 28
Follow-along lab: Watch intervals catch the true mean
Run: python 02_lab_watch_intervals_catch_the_true_mean.py
"""
from random import gauss, seed
from statistics import mean, stdev
seed(0)
hits = 0
for _ in range(1000):
    xs = [gauss(50, 10) for _ in range(30)]
    m, sd = mean(xs), stdev(xs)
    half = 1.96 * sd / 30 ** 0.5
    if m - half <= 50 <= m + half:
        hits += 1
print("true mean: 50")
print("intervals built: 1000")
print("contain the truth:", hits)
print("coverage:", hits / 1000)
