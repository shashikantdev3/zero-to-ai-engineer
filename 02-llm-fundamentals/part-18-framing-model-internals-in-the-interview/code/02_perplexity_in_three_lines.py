"""Zero to AI Engineer · LLM Fundamentals · Part 18 of 18
Slide: Perplexity in Three Lines
Run: python 02_perplexity_in_three_lines.py
"""
# Needs: pip install numpy
import numpy as np
# logprob of each real token
lp = np.array([-0.2, -1.5, -0.7, -3.0])
ppl = np.exp(-lp.mean())
print(round(ppl, 2))
