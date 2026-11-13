"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 2 of 28
Slide: Dropout in PyTorch
Run: python 02_dropout_in_pytorch.py
"""
# Needs: pip install torch
import torch.nn as nn

net = nn.Sequential(
    nn.Linear(64, 128),
    nn.ReLU(),
    nn.Dropout(p=0.3),
    nn.Linear(128, 2),
)
# dropout active
net.train()
# dropout off for validation and serving
net.eval()
