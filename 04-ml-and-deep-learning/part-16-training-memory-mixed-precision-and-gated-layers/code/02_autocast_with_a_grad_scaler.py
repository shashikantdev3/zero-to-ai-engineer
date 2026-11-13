"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 16 of 28
Slide: Autocast with a grad scaler
Run: python 02_autocast_with_a_grad_scaler.py
"""
# Needs: pip install torch
import torch
from torch.nn.functional import cross_entropy
model = torch.nn.Linear(4, 2)
opt = torch.optim.SGD(
    model.parameters(), lr=0.1)
xb = torch.randn(8, 4)
yb = torch.randint(0, 2, (8,))
# needed for fp16, usually not for bf16
scaler = torch.amp.GradScaler("cuda")
# weights stay fp32, cast per op
with torch.autocast("cuda", torch.float16):
    loss = cross_entropy(model(xb), yb)
