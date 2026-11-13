"""Zero to AI Engineer · LLM Fundamentals · Part 1 of 18
Slide: A Toy Model and Sampler
Run: python 01_a_toy_model_and_sampler.py
"""
import math, random
VOCAB = ["the", "cat", "sat", "<eos>"]

def model(tokens):
    # made-up next-token scores (logits)
    return [1.0, 2.0, 1.5, 0.5 * len(tokens)]

def sample(logits, temp=0.7):
    w = [math.exp(s / temp) for s in logits]
    return random.choices(range(4), w)[0]
