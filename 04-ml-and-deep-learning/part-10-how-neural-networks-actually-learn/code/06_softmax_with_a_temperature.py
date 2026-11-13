"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 10 of 28
Slide: Softmax with a temperature
Run: python 06_softmax_with_a_temperature.py
"""
# Needs: pip install numpy
import numpy as np

def softmax(z, temperature=1.0):
    z = np.asarray(z) / temperature
    # subtract max for numerical stability
    e = np.exp(z - z.max())
    return e / e.sum()

logits = [2.0, 1.0, 0.1]
print(softmax(logits))
print(softmax(logits, temperature=0.5))
