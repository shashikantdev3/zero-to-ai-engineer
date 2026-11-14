"""Zero to AI Engineer · RAG and Vector Search · Part 3 of 26
Slide: An IVF index in Faiss
Run: python 05_an_ivf_index_in_faiss.py
"""
# Needs: pip install faiss-cpu numpy
import faiss
import numpy as np
d, nlist = 768, 1024
rng = np.random.default_rng(0)
xb = rng.random((40000, d), dtype=np.float32)
xq = xb[:3]
quant = faiss.IndexFlatL2(d)
index = faiss.IndexIVFFlat(quant, d, nlist)
index.train(xb)
index.add(xb)
index.nprobe = 16
distances, ids = index.search(xq, 10)
