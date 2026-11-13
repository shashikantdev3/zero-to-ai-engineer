"""Zero to AI Engineer · LLM Fundamentals · Part 8 of 18
Slide: A feed-forward network in NumPy
Run: python 01_a_feed_forward_network_in_numpy.py
"""
# Needs: pip install numpy
import numpy as np

# x: (n, d_model)
# W1: (d_model, 4 * d_model)
def ffn(x, W1, b1, W2, b2):
    # ReLU, as in the original transformer
    h = np.maximum(0, x @ W1 + b1)
    return h @ W2 + b2
