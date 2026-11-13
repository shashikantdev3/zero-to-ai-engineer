"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 28 of 28
Slide: A Tiny Labelled Table
Run: python 07_a_tiny_labelled_table.py
"""
# Needs: pip install numpy pandas
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
