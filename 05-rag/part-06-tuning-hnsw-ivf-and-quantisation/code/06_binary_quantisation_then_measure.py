"""Zero to AI Engineer · RAG and Vector Search · Part 6 of 26
Slide: Binary quantisation, then measure
Run: python 06_binary_quantisation_then_measure.py
"""
# Qdrant settings, mirrored as plain dicts
quant = {"binary": {"always_ram": True}}
params = {"quantization": {
    "rescore": True, "oversampling": 3.0}}
# quant at creation, params on each query
exact = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
approx = [1, 2, 3, 5, 4, 7, 6, 9, 12, 15]
hits = len(set(exact) & set(approx))
print(f"recall@10 = {hits / 10:.1f}")
