"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 15 of 28
Slide: Linear warmup into cosine decay
Run: python 04_linear_warmup_into_cosine_decay.py
"""
# Needs: pip install torch
import torch
from torch.optim import lr_scheduler as S
model = torch.nn.Linear(4, 1)
opt = torch.optim.AdamW(model.parameters())
total_steps = 10_000
warm = S.LinearLR(opt, start_factor=0.01,
                  total_iters=500)
cos = S.CosineAnnealingLR(
    opt, T_max=total_steps - 500)
sched = S.SequentialLR(
    opt, [warm, cos], milestones=[500])
print(sched.get_last_lr())
