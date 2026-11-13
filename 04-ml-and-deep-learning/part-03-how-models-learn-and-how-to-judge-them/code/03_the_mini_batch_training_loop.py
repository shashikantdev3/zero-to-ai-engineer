"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 3 of 28
Slide: The Mini-Batch Training Loop
Run: python 03_the_mini_batch_training_loop.py
"""
# Needs: pip install torch
# --- repeated from 02_setting_up_a_pytorch_run.py so this file runs on its own ---
import torch
from torch.utils import data
X = torch.randn(512, 4)
Y = X.sum(dim=1, keepdim=True)
ds = data.TensorDataset(X, Y)
model = torch.nn.Linear(4, 1)
loss_fn = torch.nn.MSELoss()
p = model.parameters()
opt = torch.optim.SGD(p, lr=0.01)

# --- this slide ---
loader = data.DataLoader(ds, batch_size=256,
                         shuffle=True)
for xb, yb in loader:
    # clear last batch's gradients
    opt.zero_grad()
    loss_fn(model(xb), yb).backward()
    opt.step()
