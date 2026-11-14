"""Zero to AI Engineer · RAG and Vector Search · Part 6 of 26
Slide: Build IVFFlat after loading
Run: python 02_build_ivfflat_after_loading.py
"""
import math
rows = 1_000_000
# load rows first: centres come from them
lists = rows // 1000
probes = round(math.sqrt(lists))
build = (
    "CREATE INDEX ON chunks USING ivfflat "
    "(embedding vector_cosine_ops) "
    f"WITH (lists = {lists});"
)
print(build)
print(f"SET ivfflat.probes = {probes};")
