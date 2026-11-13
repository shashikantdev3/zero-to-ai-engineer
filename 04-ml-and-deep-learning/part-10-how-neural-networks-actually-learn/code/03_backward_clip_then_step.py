"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 10 of 28
Slide: Backward, clip, then step
Run: python 03_backward_clip_then_step.py
"""
# Needs: pip install torch
import torch
from torch import nn
from torch.nn.utils import clip_grad_norm_
model = nn.Linear(4, 1)
params = list(model.parameters())
opt = torch.optim.SGD(params, lr=0.1)
x, y = torch.randn(8, 4), torch.randn(8, 1)
loss = ((model(x) - y) ** 2).mean()
loss.backward()
clip_grad_norm_(params, max_norm=1.0)
opt.step()
