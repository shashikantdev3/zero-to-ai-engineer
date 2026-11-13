"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 10 of 28
Slide: Both layers in PyTorch
Run: python 05_both_layers_in_pytorch.py
"""
# Needs: pip install torch
import torch
from torch import nn
# common in CNNs and MLPs
bn = nn.BatchNorm1d(64)
# standard in transformer blocks
ln = nn.LayerNorm(512)
print(ln(torch.randn(1, 512)).shape)
# one example: needs eval mode
bn.eval()
print(bn(torch.randn(1, 64)).shape)
