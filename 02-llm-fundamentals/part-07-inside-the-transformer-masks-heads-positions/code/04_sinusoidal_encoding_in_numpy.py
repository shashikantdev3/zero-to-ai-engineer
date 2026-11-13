"""Zero to AI Engineer · LLM Fundamentals · Part 7 of 18
Slide: Sinusoidal encoding in NumPy
Run: python 04_sinusoidal_encoding_in_numpy.py
"""
# Needs: pip install numpy
import numpy as np

def sinusoidal(n_pos, d_model):
    # d_model must be even
    pos = np.arange(n_pos)[:, None]
    i = np.arange(0, d_model, 2)[None, :]
    angle = pos / (10000 ** (i / d_model))
    pe = np.zeros((n_pos, d_model))
    pe[:, 0::2] = np.sin(angle)
    pe[:, 1::2] = np.cos(angle)
    return pe
print(sinusoidal(4, 8).shape)
