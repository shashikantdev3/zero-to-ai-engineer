"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 3 of 28
Slide: AdamW With a Cosine Schedule
Run: python 04_adamw_with_a_cosine_schedule.py
"""
# Needs: pip install torch
import torch
from torch.optim import lr_scheduler
model = torch.nn.Linear(4, 1)
num_steps = 100
params = model.parameters()
opt = torch.optim.AdamW(params, lr=3e-4)
sched = lr_scheduler.CosineAnnealingLR(
    opt, T_max=num_steps)
for step in range(num_steps):
    opt.step()
    sched.step()
print(sched.get_last_lr())
