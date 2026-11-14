"""Zero to AI Engineer · RAG and Vector Search · Part 15 of 26
Slide: Reranking with a cross-encoder
Run: python 03_reranking_with_a_cross_encoder.py
"""
# Needs: pip install sentence-transformers
# (not run while building this repo, because the package was not installed there)
from sentence_transformers import CrossEncoder
name = "cross-encoder/ms-marco-MiniLM-L-6-v2"
reranker = CrossEncoder(name)
query = "Am I eligible for a refund?"
candidates = ["Refunds within 30 days.",
              "Sale items are not eligible.",
              "Shipping takes 5 days."]
pairs = [(query, c) for c in candidates]
scores = reranker.predict(pairs)
ranked = sorted(zip(scores, candidates),
                key=lambda p: -p[0])
top = [c for _, c in ranked][:5]
