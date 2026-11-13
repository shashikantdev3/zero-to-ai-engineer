"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 16 of 28
Slide: The scaled backward step
Run: python 03_the_scaled_backward_step.py
"""
# Needs: pip install torch
# --- repeated from 02_autocast_with_a_grad_scaler.py so this file runs on its own ---
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

# --- this slide ---
# scale the loss so tiny grads survive
scaler.scale(loss).backward()
scaler.step(opt)
scaler.update()
