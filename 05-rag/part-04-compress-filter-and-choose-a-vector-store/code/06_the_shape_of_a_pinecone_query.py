"""Zero to AI Engineer · RAG and Vector Search · Part 4 of 26
Slide: The shape of a Pinecone query
Run: python 06_the_shape_of_a_pinecone_query.py
"""
# Illustrative shape, not a live call.
# A real client reads its key from an
# environment variable, never from code.
qvec = [0.01, 0.02]
query = {
    "vector": qvec,
    "top_k": 10,
    "namespace": "tenant-a",
    "filter": {"department": {"$eq": "hr"}},
    "include_metadata": True,
}
print(sorted(query))
