"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 7 of 28
Slide: No Missing Values, No Infinity
Run: python 02_no_missing_values_no_infinity.py
"""
# Needs: pip install numpy pandas
# --- repeated from 01_a_past_only_average.py so this file runs on its own ---
import numpy as np
import pandas as pd
df = pd.DataFrame({
    "txn_id": [1, 2, 3, 4],
    "customer": ["a", "a", "b", "a"],
    "ts": [10, 20, 30, 40],
    "amount": [50.0, 70.0, 20.0, 600.0]})
# ties broken by id: deterministic order
df = df.sort_values(["ts", "txn_id"])
g = df.groupby("customer")["amount"]
past_avg = g.transform(
    lambda s: s.shift(1).expanding().mean())

# --- this slide ---
df["is_first_txn"] = past_avg.isna()
# mean from the training period only
train_mean_amount = 60.0
past_avg = past_avg.replace(0, np.nan)
past_avg = past_avg.fillna(train_mean_amount)
# no NaN, no divide by zero
df["amt_vs_avg"] = df["amount"] / past_avg
df["log_amount"] = np.log1p(df["amount"])
print(df)
