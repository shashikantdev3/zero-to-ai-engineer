"""Zero to AI Engineer · RAG and Vector Search · Part 4 of 26
Slide: Product quantisation in Faiss
Run: python 01_product_quantisation_in_faiss.py
"""
# Needs: pip install faiss-cpu
import faiss
d = 768
q = faiss.IndexFlatL2(d)
# nlist lists, m sub-vectors, nbits per code
nlist, m, nbits = 1024, 64, 8
ix = faiss.IndexIVFPQ(q, d, nlist, m, nbits)
# 64 sub-vectors x 8 bits = 64 bytes
print("PQ bytes:", m * nbits // 8)
print("float32 bytes:", d * 4)
