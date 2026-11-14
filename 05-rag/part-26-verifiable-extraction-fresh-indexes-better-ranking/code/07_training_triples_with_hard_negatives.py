"""Zero to AI Engineer · RAG and Vector Search · Part 26 of 26
Slide: Training triples with hard negatives
Run: python 07_training_triples_with_hard_negatives.py
"""
# Needs: pip install sentence-transformers
# (not run while building this repo, because the package was not installed there)
from sentence_transformers import (
    SentenceTransformer, InputExample, losses)

# mined from logs, then reviewed
triples = [("What is form PX-7?",
            "PX-7 is the travel claim form.",
            "PX-9 is the leave request form.")]
train = [InputExample(texts=[
    f"query: {q}", f"passage: {pos}",
    f"passage: {neg}"])
    for q, pos, neg in triples]
