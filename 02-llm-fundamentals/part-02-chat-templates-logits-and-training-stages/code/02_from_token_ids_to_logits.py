"""Zero to AI Engineer · LLM Fundamentals · Part 2 of 18
Slide: From Token IDs to Logits
Run: python 02_from_token_ids_to_logits.py
"""
# Needs: pip install numpy
import numpy as np

vocab, d_model = 50_000, 768
# learned in real training
E = np.random.randn(vocab, d_model) * 0.02
# three token IDs give shape (3, 768)
x = E[[312, 9021, 77]]
# weight tying, if the model uses it
W_out = E.T
# one score per vocabulary token
logits = x[-1] @ W_out
print(x.shape, logits.shape)
