"""Zero to AI Engineer · RAG and Vector Search · Part 8 of 26
Slide: Timing a full rebuild
Run: python 04_timing_a_full_rebuild.py
"""
import time
def rebuild_index(source, embeddings, target):
    # stand-in for the real rebuild job
    time.sleep(0.1)
t0 = time.monotonic()
rebuild_index(source="documents",
              embeddings="stored",
              target="docs-rebuild-test")
hours = (time.monotonic() - t0) / 3600
# record this as the recovery time objective
print(f"full rebuild: {hours:.1f} h")
