"""Zero to AI Engineer · LLM Fundamentals · Part 10 of 18
Slide: Counting a Llama 3 8B style layer
Run: python 04_counting_a_llama_3_8b_style_layer.py
"""
d, ffn, kv_dim = 4096, 14336, 8 * 128
# q, o full; k, v shrunk by GQA
attn = 2 * d * d + 2 * d * kv_dim
# SwiGLU: W1, W3, W2
mlp = 3 * d * ffn
print(attn / 1e6, mlp / 1e6)
print(mlp / (attn + mlp))
