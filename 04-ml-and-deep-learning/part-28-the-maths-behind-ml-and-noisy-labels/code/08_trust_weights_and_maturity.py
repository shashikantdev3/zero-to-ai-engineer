"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 28 of 28
Slide: Trust, Weights and Maturity
Run: python 08_trust_weights_and_maturity.py
"""
# Needs: pip install numpy pandas
# --- repeated from 07_a_tiny_labelled_table.py so this file runs on its own ---
import numpy as np
import pandas as pd
df = pd.DataFrame({
    "ts": [1, 2, 3, 4, 5, 6],
    "y": [1, 0, 1, 0, 1, 0],
    "reason_code": ["F1", None, "D9",
                    None, "F1", None]})
# illustrations: agree with the fraud team
TRUSTED_FRAUD_CODES = ["F1"]
maturity = 2

# --- this slide ---
label_ok = (df["reason_code"]
            .isin(TRUSTED_FRAUD_CODES)
            | (df["y"] == 0))
# illustration: down-weight low-trust fraud
weights = np.where(label_ok, 1.0, 0.5)
immature = df.ts >= df.ts.max() - maturity
# immature rows: unlabelled, not legit
train_rows = df[~immature]
print(weights)
print(len(train_rows))
