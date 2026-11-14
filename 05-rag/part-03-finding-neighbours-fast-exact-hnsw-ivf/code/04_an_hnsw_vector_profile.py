"""Zero to AI Engineer · RAG and Vector Search · Part 3 of 26
Slide: An HNSW vector profile
Run: python 04_an_hnsw_vector_profile.py
"""
# Azure AI Search, values illustrative
hnsw = {
    "m": 4,
    "efConstruction": 400,
    "efSearch": 500,
    "metric": "cosine",
}
vector_search = {"algorithms": [{
    "name": "hnsw-default",
    "kind": "hnsw",
    "hnswParameters": hnsw,
}]}
