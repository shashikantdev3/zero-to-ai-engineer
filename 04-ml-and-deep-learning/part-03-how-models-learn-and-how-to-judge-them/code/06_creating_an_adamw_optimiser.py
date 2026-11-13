"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 3 of 28
Slide: Creating an AdamW Optimiser
Run: python 06_creating_an_adamw_optimiser.py
"""
# Needs: pip install torch
import torch
model = torch.nn.Linear(4, 1)
opt = torch.optim.AdamW(
    model.parameters(),
    lr=1e-3,
    betas=(0.9, 0.999),
    weight_decay=0.01,
)
