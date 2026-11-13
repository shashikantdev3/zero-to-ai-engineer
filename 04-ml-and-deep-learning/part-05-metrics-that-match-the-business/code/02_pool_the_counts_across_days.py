"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 5 of 28
Slide: Pool the counts across days
Run: python 02_pool_the_counts_across_days.py
"""
# Needs: pip install numpy pandas
# --- repeated from 01_sample_data_and_running_totals.py so this file runs on its own ---
import numpy as np
import pandas as pd
df = pd.DataFrame({
    "day": [1, 1, 1, 2, 2, 2],
    "y": [1, 0, 1, 0, 1, 0],
    "score": [.9, .8, .3, .7, .6, .1],
    "amount": [500, 20, 80, 30, 900, 10]})
k = 2
caught = total = 0.0
caught_rs = total_rs = 0.0
no_fraud = []

# --- this slide ---
for day, g in df.groupby("day"):
    y = g["y"].to_numpy()
    s = g["score"].to_numpy()
    amt = g["amount"].to_numpy()
    if y.sum() == 0:
        no_fraud.append(day); continue
    top = np.argsort(-s)[:k]
    caught += y[top].sum()
    total += y.sum()
    caught_rs += (amt[top] * y[top]).sum()
    total_rs += (amt * y).sum()
print(caught / total, caught_rs / total_rs)
