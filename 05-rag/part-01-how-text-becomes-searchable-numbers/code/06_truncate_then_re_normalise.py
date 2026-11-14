"""Zero to AI Engineer · RAG and Vector Search · Part 1 of 26
Slide: Truncate, Then Re-normalise
Run: python 06_truncate_then_re_normalise.py
"""
# Needs: pip install numpy
import numpy as np

vec = [3.0, 4.0, 0.0, 0.0]
v = np.asarray(vec, dtype=np.float32)
# only if you truncate yourself,
# and only for models trained for it
v = v[:2]
n = np.linalg.norm(v)
# guard against a zero vector
v = v / n if n else v
print(v, np.linalg.norm(v))
