"""Zero to AI Engineer · RAG and Vector Search · Part 1 of 26
Slide: Query Side With a Prefix
Run: python 03_query_side_with_a_prefix.py
"""
# Needs: pip install sentence-transformers
# (not run while building this repo, because the package was not installed there)
import sentence_transformers as st

model = st.SentenceTransformer(
    "intfloat/e5-base-v2")

def embed_query(q):
    return model.encode(
        f"query: {q}",
        normalize_embeddings=True)

v = embed_query("reset my VPN password")
print(len(v))
