"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 9 of 28
Slide: A multilayer perceptron in PyTorch
Run: python 07_a_multilayer_perceptron_in_pytorch.py
"""
# Needs: pip install torch
import torch
import torch.nn as nn
mlp = nn.Sequential(
    nn.Linear(30, 64), nn.ReLU(),
    nn.Linear(64, 64), nn.ReLU(),
    nn.Linear(64, 2))
x = torch.randn(4, 30)
print(mlp(x).shape)
