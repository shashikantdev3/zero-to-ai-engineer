"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 2 of 28
Slide: Weighted cross-entropy in PyTorch
Run: python 05_weighted_cross_entropy_in_pytorch.py
"""
# Needs: pip install torch
import torch
import torch.nn as nn
# class 1 is rare, so weight it 10 times
w = torch.tensor([1.0, 10.0])
# takes raw logits
loss_fn = nn.CrossEntropyLoss(weight=w)
logits = torch.tensor([[2.0, -1.0],
                       [0.5, 1.5]])
targets = torch.tensor([0, 1])
# do NOT apply softmax before this
loss = loss_fn(logits, targets)
print(loss.item())
