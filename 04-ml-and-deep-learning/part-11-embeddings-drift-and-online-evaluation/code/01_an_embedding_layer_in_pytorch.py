"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 11 of 28
Slide: An embedding layer in PyTorch
Run: python 01_an_embedding_layer_in_pytorch.py
"""
# Needs: pip install torch
import torch
import torch.nn as nn

# e.g. ten thousand merchant IDs
emb = nn.Embedding(
    num_embeddings=10_000,
    embedding_dim=32,
)
ids = torch.tensor([12, 845])
vecs = emb(ids)
# shape (2, 32): one row per ID
print(vecs.shape)
