"""Zero to AI Engineer · RAG and Vector Search · Part 7 of 26
Slide: Index the Filter Field
Run: python 02_index_the_filter_field.py
"""
# Needs: pip install qdrant_client
# (not run while building this repo, because the package was not installed there)
from qdrant_client import QdrantClient, models
client = QdrantClient(":memory:")
cfg = models.VectorParams(
    size=4, distance=models.Distance.COSINE)
client.create_collection(
    "docs", vectors_config=cfg)
# index the filter field for the planner
kw = models.PayloadSchemaType.KEYWORD
client.create_payload_index(
    "docs", field_name="tenant_id",
    field_schema=kw)
