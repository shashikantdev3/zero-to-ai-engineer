"""Zero to AI Engineer · LLM Fundamentals · Part 8 of 18
Slide: KV cache maths in Python
Run: python 03_kv_cache_maths_in_python.py
"""
def kv_bytes(tokens, layers=32, kv_heads=8,
        head_dim=128, bytes_per=2, seqs=1):
    return (2 * layers * kv_heads * head_dim
            * bytes_per * tokens * seqs)
# ~131 KB per token
print(kv_bytes(1) / 1e3)
# ~393 MB, one user
print(kv_bytes(3_000) / 1e6)
# ~39.3 GB, 100 users
print(kv_bytes(3_000, seqs=100) / 1e9)
# ~16 GB of 16-bit weights
print(8e9 * 2 / 1e9)
