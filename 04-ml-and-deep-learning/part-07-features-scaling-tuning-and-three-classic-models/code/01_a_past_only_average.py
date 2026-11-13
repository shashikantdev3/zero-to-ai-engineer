"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 7 of 28
Slide: A Past-Only Average
Run: python 01_a_past_only_average.py
"""
# Needs: pip install numpy pandas
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
