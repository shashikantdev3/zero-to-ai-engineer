"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 10 of 28
Slide: Activations and the output rule
Run: python 01_activations_and_the_output_rule.py
"""
# Needs: pip install torch
import torch
from torch import nn
x = torch.tensor([-2.0, 0.0, 2.0])
print(nn.ReLU()(x))
print(nn.GELU()(x))
print(nn.Sigmoid()(x))
# Output layer: raw logits, no activation.
# Multi-class: CrossEntropyLoss on logits.
# Binary: BCEWithLogitsLoss on logits.
logits = torch.tensor([[2.0, 0.5, -1.0]])
target = torch.tensor([0])
print(nn.CrossEntropyLoss()(logits, target))
