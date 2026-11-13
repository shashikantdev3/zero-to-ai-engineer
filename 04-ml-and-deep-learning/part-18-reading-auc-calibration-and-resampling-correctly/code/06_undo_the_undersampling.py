"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 18 of 28
Slide: Undo the undersampling
Run: python 06_undo_the_undersampling.py
"""
import math

def unsample(p_s, beta):
    # beta = fraction of negatives kept
    return beta * p_s / (beta * p_s - p_s + 1)

print(unsample(0.5, beta=0.1))

def logit(q):
    return math.log(q / (1 - q))
z = logit(0.5) + math.log(0.1)
print(1 / (1 + math.exp(-z)))
