"""Zero to AI Engineer · Fine-tuning and Model Choice · Part 2 of 10
Slide: One pair, one margin
Run: python 01_one_pair_one_margin.py
"""
import math
# one row for TRL's DPOTrainer
row = {"prompt": "Capital of Mars?",
       "chosen": "I do not know.",
       "rejected": "Olympus City."}
# log-prob: model minus frozen reference
gap_c = -5.5 - (-5.0)
gap_r = -9.0 - (-6.0)
beta = 0.1
margin = beta * (gap_c - gap_r)
loss = math.log(1 + math.exp(-margin))
print(round(margin, 2), round(loss, 3))
