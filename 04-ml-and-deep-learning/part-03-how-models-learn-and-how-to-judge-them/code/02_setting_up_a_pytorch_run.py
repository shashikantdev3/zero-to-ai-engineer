"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 3 of 28
Slide: Setting Up a PyTorch Run
Run: python 02_setting_up_a_pytorch_run.py
"""
# Needs: pip install torch
import torch
from torch.utils import data
X = torch.randn(512, 4)
Y = X.sum(dim=1, keepdim=True)
ds = data.TensorDataset(X, Y)
model = torch.nn.Linear(4, 1)
loss_fn = torch.nn.MSELoss()
p = model.parameters()
opt = torch.optim.SGD(p, lr=0.01)
