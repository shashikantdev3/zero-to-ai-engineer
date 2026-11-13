"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 22 of 28
Slide: Accuracy by week and segment
Run: python 04_accuracy_by_week_and_segment.py
"""
# Needs: pip install pandas
import pandas as pd
df = pd.DataFrame({
  "week": [1, 1, 2, 2],
  "segment": ["a", "b", "a", "b"],
  "correct": [1, 1, 1, 0],
  "feature_x": [0.5, 0.7, 0.4, None]})
by = df.groupby(["week", "segment"]).agg(
  acc=("correct", "mean"),
  n=("correct", "size"),
  null_rate=("feature_x",
             lambda s: s.isna().mean()))
print(by.unstack("segment"))
