"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 1 of 28
Slide: Drop unripe rows, set the cut-offs
Run: python 01_drop_unripe_rows_set_the_cut_offs.py
"""
# Needs: pip install pandas
import pandas as pd
d = pd.date_range("2025-08-01", periods=500)
df = pd.DataFrame({"ts": d, "fraud": 0})
# agree this window with the business
maturity = pd.Timedelta(days=60)
df = df.sort_values("ts")
# drop rows whose labels are not mature
df = df[df.ts < df.ts.max() - maturity]
train_end = pd.Timestamp("2026-02-01")
val_start = train_end + maturity
val_end = val_start + pd.Timedelta(days=30)
test_start = val_end + maturity
