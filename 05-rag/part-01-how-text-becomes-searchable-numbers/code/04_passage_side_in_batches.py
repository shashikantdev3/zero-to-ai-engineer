"""Zero to AI Engineer · RAG and Vector Search · Part 1 of 26
Slide: Passage Side in Batches
Run: python 04_passage_side_in_batches.py
"""
# Needs: pip install sentence-transformers
# (not run while building this repo, because the package was not installed there)
# --- repeated from 03_query_side_with_a_prefix.py so this file runs on its own ---
import sentence_transformers as st

model = st.SentenceTransformer(
    "intfloat/e5-base-v2")

def embed_query(q):
    return model.encode(
        f"query: {q}",
        normalize_embeddings=True)

v = embed_query("reset my VPN password")
print(len(v))

# --- this slide ---
def embed_passages(ps):
    texts = [f"passage: {p}" for p in ps]
    return model.encode(
        texts, batch_size=64,
        normalize_embeddings=True)

docs = ["Remote access credential recovery",
        "Expense policy for travel"]
m = embed_passages(docs)
print(m.shape)
# Before a re-embed, estimate cost:
# total_tokens x price_per_token vs budget
