"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 5 of 28
Slide: Sample data and running totals
Run: python 01_sample_data_and_running_totals.py
"""
# Needs: pip install numpy pandas
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
