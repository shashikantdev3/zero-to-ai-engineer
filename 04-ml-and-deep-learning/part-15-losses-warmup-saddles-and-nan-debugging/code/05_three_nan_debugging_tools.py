"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 15 of 28
Slide: Three NaN debugging tools
Run: python 05_three_nan_debugging_tools.py
"""
# Needs: pip install torch
import torch
from torch import nn
model = nn.Linear(4, 1)
xb = torch.randn(8, 4)
assert torch.isfinite(xb).all(), "bad input"
# debugging only: slow, finds the failing op
torch.autograd.set_detect_anomaly(True)
loss = model(xb).pow(2).mean()
loss.backward()
nn.utils.clip_grad_norm_(
    model.parameters(), max_norm=1.0)
