"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 19 of 28
Slide: Temperature scaling in PyTorch
Run: python 02_temperature_scaling_in_pytorch.py
"""
# Needs: pip install torch
import torch, torch.nn.functional as F
logits = torch.randn(100, 3) * 4
labels = torch.randint(0, 3, (100,))
T = torch.ones(1, requires_grad=True)
opt = torch.optim.LBFGS(
    [T], lr=0.1, max_iter=50)
def closure():
    opt.zero_grad()
    l = F.cross_entropy(logits / T, labels)
    l.backward()
    return l
opt.step(closure)
