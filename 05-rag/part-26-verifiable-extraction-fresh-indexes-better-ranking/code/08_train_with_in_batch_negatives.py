"""Zero to AI Engineer · RAG and Vector Search · Part 26 of 26
Slide: Train with in-batch negatives
Run: python 08_train_with_in_batch_negatives.py
"""
# Needs: pip install sentence-transformers torch
# (not run while building this repo, because the package was not installed there)
# --- repeated from 07_training_triples_with_hard_negatives.py so this file runs on its own ---
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

# --- this slide ---
from torch.utils.data import DataLoader

name = "intfloat/e5-base-v2"
model = SentenceTransformer(name)
loader = DataLoader(train, shuffle=True,
                    batch_size=32)
MNRL = losses.MultipleNegativesRankingLoss
loss = MNRL(model)
model.fit(train_objectives=[(loader, loss)],
          epochs=1, warmup_steps=100)
# training API differs across versions
