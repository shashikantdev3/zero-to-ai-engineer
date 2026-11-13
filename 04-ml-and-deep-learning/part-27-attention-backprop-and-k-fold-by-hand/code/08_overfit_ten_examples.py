"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 27 of 28
Slide: Overfit ten examples
Run: python 08_overfit_ten_examples.py
"""
# Needs: pip install torch
# --- repeated from 07_a_tiny_model_to_debug.py so this file runs on its own ---
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

# --- this slide ---
xb, yb = next(iter(loader))
xb, yb = xb[:10], yb[:10]
for i in range(300):
    opt.zero_grad()
    loss = loss_fn(model(xb), yb)
    loss.backward()
    opt.step()
# should approach 0; if not, a code bug
print(loss.item())
