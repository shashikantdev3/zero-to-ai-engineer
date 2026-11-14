"""Zero to AI Engineer · RAG and Vector Search · Part 1 of 26
Slide: Record the Model on Every Vector
Run: python 02_record_the_model_on_every_vector.py
"""
MODEL = "text-embedding-3-small"
DIMS = 1536

record = {
    "id": "doc-1",
    "vector": [0.0] * DIMS,
    "embedding_model": MODEL,
    "dims": DIMS,
}
# later: detect a model swap
if record["embedding_model"] != MODEL:
    print("re-embed needed")
