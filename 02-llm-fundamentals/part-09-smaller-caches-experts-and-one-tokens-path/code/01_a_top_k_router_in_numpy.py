"""Zero to AI Engineer · LLM Fundamentals · Part 9 of 18
Slide: A top-k router in NumPy
Run: python 01_a_top_k_router_in_numpy.py
"""
# Needs: pip install numpy
import numpy as np

def moe_layer(x, gate_W, experts, k=2):
    # x is one token vector
    logits = x @ gate_W
    top = np.argsort(logits)[-k:]
    s = logits[top]
    w = np.exp(s - s.max())
    w /= w.sum()
    return sum(wi * experts[e](x)
               for wi, e in zip(w, top))
