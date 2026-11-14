"""Zero to AI Engineer · RAG and Vector Search · Part 1 of 26
Slide: Embedding One Sentence
Run: python 01_embedding_one_sentence.py
"""
# Needs: pip install sentence-transformers
# (not run while building this repo, because the package was not installed there)
import sentence_transformers as st

model = st.SentenceTransformer(
    "intfloat/e5-base-v2")
text = "How do I reset my VPN password?"
# query prefix: explained in concept 3
vector = model.encode(f"query: {text}")
# one fixed-length array of floats
print(len(vector))
print(vector[:5])
