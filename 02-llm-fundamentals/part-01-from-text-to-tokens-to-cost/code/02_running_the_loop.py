"""Zero to AI Engineer · LLM Fundamentals · Part 1 of 18
Slide: Running the Loop
Run: python 02_running_the_loop.py
"""
# --- repeated from 01_a_toy_model_and_sampler.py so this file runs on its own ---
import math, random
VOCAB = ["the", "cat", "sat", "<eos>"]

def model(tokens):
    # made-up next-token scores (logits)
    return [1.0, 2.0, 1.5, 0.5 * len(tokens)]

def sample(logits, temp=0.7):
    w = [math.exp(s / temp) for s in logits]
    return random.choices(range(4), w)[0]

# --- this slide ---
# the prompt is the single token "the"
tokens = [0]
for _ in range(10):
    next_id = sample(model(tokens))
    if VOCAB[next_id] == "<eos>":
        break
    tokens.append(next_id)
print(" ".join(VOCAB[i] for i in tokens))
