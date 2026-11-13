"""Zero to AI Engineer · LLM Fundamentals · Part 3 of 18
Slide: Chinchilla maths for 8B params
Run: python 01_chinchilla_maths_for_8b_params.py
"""
params = 8e9
# about 160 billion tokens
chinchilla_tokens = 20 * params
# rough estimate only: about 7.7e21 FLOPs
train_flops = 6 * params * chinchilla_tokens
print(f"tokens: {chinchilla_tokens:.1e}")
print(f"flops: {train_flops:.1e}")
