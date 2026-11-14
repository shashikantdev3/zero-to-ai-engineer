"""Zero to AI Engineer · RAG and Vector Search · Part 16 of 26
Slide: Two plain splitters
Run: python 04_two_plain_splitters.py
"""
from types import SimpleNamespace as NS

def split_by_headings(doc):
    return doc.text.split("\n## ")

def recursive_split(doc):
    t = doc.text
    return [t[i:i + 500]
            for i in range(0, len(t), 500)]

doc = NS(type="xlsx", headers="item | days",
         rows=["annual leave | 30"])
