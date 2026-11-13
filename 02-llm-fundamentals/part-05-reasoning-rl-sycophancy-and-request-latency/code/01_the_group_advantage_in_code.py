"""Zero to AI Engineer · LLM Fundamentals · Part 5 of 18
Slide: The Group Advantage in Code
Run: python 01_the_group_advantage_in_code.py
"""
# Needs: pip install numpy
import numpy as np

# checker scores for 8 samples of one prompt
rewards = np.array([1, 0, 0, 1, 1, 0, 0, 0])
mean, spread = rewards.mean(), rewards.std()
adv = (rewards - mean) / (spread + 1e-6)
# correct answers positive, wrong negative
print(adv.round(2))
