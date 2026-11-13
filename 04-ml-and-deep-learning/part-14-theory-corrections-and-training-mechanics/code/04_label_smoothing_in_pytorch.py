"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 14 of 28
Slide: Label smoothing in PyTorch
Run: python 04_label_smoothing_in_pytorch.py
"""
# Needs: pip install torch
import torch
from torch import nn
# label_smoothing needs PyTorch 1.10+
loss_fn = nn.CrossEntropyLoss(
    label_smoothing=0.1)
logits = torch.tensor([[4.0, 0.5, 0.2]])
target = torch.tensor([0])
print(loss_fn(logits, target))
