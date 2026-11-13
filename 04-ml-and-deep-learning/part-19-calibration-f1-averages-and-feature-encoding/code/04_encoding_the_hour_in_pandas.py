"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 19 of 28
Slide: Encoding the hour in pandas
Run: python 04_encoding_the_hour_in_pandas.py
"""
# Needs: pip install numpy pandas
import numpy as np
import pandas as pd
df = pd.DataFrame({"hour": [0, 3, 9, 12, 23]})
angle = 2 * np.pi * df["hour"] / 24
df["hour_sin"] = np.sin(angle)
df["hour_cos"] = np.cos(angle)
print(df.round(3))
