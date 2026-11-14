"""Zero to AI Engineer · RAG and Vector Search · Part 10 of 26
Follow-along lab: An idempotent sync job
Run: python 04_lab_an_idempotent_sync_job.py
"""
import zlib
index = {}
def sync(doc, chunks):
    new = {}
    for n, t in enumerate(chunks):
        h = zlib.crc32(t.encode())
        new[f"{doc}#{n}#{h}"] = t
    for k in list(index):
        if k.startswith(doc) and k not in new:
            del index[k]
    index.update(new)
for run in ("ab", "ab", "ac", ""):
    sync("leave", list(run))
    print(repr(run), len(index), "chunks")
