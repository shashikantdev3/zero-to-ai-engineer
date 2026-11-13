"""Zero to AI Engineer · LLM Fundamentals · Part 10 of 18
Slide: SwiGLU in a few lines
Run: python 05_swiglu_in_a_few_lines.py
"""
# Needs: pip install numpy
import numpy as np

def swiglu(x, W1, W3, W2):
    a = x @ W1
    # Swish of a
    swish = a / (1 + np.exp(-a))
    # gate branch, elementwise
    return (swish * (x @ W3)) @ W2
