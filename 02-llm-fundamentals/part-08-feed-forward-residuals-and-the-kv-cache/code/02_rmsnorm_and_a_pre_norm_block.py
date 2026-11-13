"""Zero to AI Engineer · LLM Fundamentals · Part 8 of 18
Slide: RMSNorm and a pre-norm block
Run: python 02_rmsnorm_and_a_pre_norm_block.py
"""
# Needs: pip install numpy
import numpy as np

def rms_norm(x, g, eps=1e-6):
    sq = (x ** 2).mean(-1, keepdims=True)
    return x / np.sqrt(sq + eps) * g

# pre-norm transformer block
def block(x, attn, ffn, g1, g2):
    x = x + attn(rms_norm(x, g1))
    x = x + ffn(rms_norm(x, g2))
    return x
