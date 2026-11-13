"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 24 of 28
Slide: Allocation Share per Day
Run: python 03_allocation_share_per_day.py
"""
# Needs: pip install pandas
import pandas as pd

df = pd.DataFrame({
    "day": ["Thu"] * 2 + ["Fri"] * 3,
    "arm": ["A", "B", "A", "A", "A"],
})
# allocation share per day: should be flat
share = pd.crosstab(df["day"], df["arm"],
                    normalize="index")
print(share)
