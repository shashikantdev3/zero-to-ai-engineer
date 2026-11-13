"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 16 of 28
Slide: A SwiGLU block in PyTorch
Run: python 05_a_swiglu_block_in_pytorch.py
"""
# Needs: pip install torch
import torch
from torch import nn
class SwiGLU(nn.Module):
    def __init__(self, d, h):
        super().__init__()
        self.w1 = nn.Linear(d, h)
        self.w2 = nn.Linear(d, h)
        self.w3 = nn.Linear(h, d)
    def forward(self, x):
        a = nn.functional.silu(self.w1(x))
        return self.w3(a * self.w2(x))
print(SwiGLU(8, 16)(torch.randn(2, 8)).shape)
