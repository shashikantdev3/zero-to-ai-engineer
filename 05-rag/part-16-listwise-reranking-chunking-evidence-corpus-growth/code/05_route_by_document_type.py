"""Zero to AI Engineer · RAG and Vector Search · Part 16 of 26
Slide: Route by document type
Run: python 05_route_by_document_type.py
"""
# --- repeated from 04_two_plain_splitters.py so this file runs on its own ---
from types import SimpleNamespace as NS

def split_by_headings(doc):
    return doc.text.split("\n## ")

def recursive_split(doc):
    t = doc.text
    return [t[i:i + 500]
            for i in range(0, len(t), 500)]

doc = NS(type="xlsx", headers="item | days",
         rows=["annual leave | 30"])

# --- this slide ---
SPLITTERS = {
    "pdf_policy": split_by_headings,
    "xlsx": lambda d: [f"{d.headers}\n{r}"
                       for r in d.rows],
    "slides": lambda d: [
        f"{d.title} > {s.title}\n{s.text}"
        for s in d.slides],
}
fn = SPLITTERS.get(doc.type, recursive_split)
for c in fn(doc):
    print({"chunker": doc.type, "text": c})
