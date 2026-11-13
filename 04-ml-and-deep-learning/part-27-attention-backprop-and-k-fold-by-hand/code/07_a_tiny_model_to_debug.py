"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 27 of 28
Slide: A tiny model to debug
Run: python 07_a_tiny_model_to_debug.py
"""
# Needs: pip install torch
import torch
from torch import nn
torch.manual_seed(0)
X, y = torch.randn(64, 4), torch.randn(64, 1)
loader = torch.utils.data.DataLoader(
    list(zip(X, y)), batch_size=16)
model = nn.Sequential(nn.Linear(4, 64),
    nn.ReLU(), nn.Linear(64, 1))
params = model.parameters()
opt = torch.optim.Adam(params, lr=0.01)
loss_fn = nn.MSELoss()
