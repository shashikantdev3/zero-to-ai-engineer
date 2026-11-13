"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 16 of 28
Slide: Checkpointing each block
Run: python 01_checkpointing_each_block.py
"""
# Needs: pip install torch
import torch
from torch import nn
from torch.utils.checkpoint import checkpoint
blocks = nn.ModuleList(
    nn.Linear(8, 8) for _ in range(4))
x = torch.randn(2, 8, requires_grad=True)
for block in blocks:
    # recompute in backward
    x = checkpoint(
        block, x, use_reentrant=False)
x.sum().backward()
print("backward ran")
