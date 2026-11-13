"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 15 of 28
Slide: Triplet margin loss in PyTorch
Run: python 03_triplet_margin_loss_in_pytorch.py
"""
# Needs: pip install torch
import torch
from torch import nn
torch.manual_seed(0)
anchor = torch.randn(4, 8)
positive = anchor + 0.1 * torch.randn(4, 8)
negative = torch.randn(4, 8)
loss_fn = nn.TripletMarginLoss(margin=0.2)
loss = loss_fn(anchor, positive, negative)
print(loss.item())
