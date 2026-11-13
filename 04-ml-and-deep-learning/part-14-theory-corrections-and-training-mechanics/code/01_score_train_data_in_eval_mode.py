"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 14 of 28
Slide: Score train data in eval mode
Run: python 01_score_train_data_in_eval_mode.py
"""
# Needs: pip install torch
import torch
from torch import nn
model = nn.Sequential(
    nn.Linear(4, 2), nn.Dropout(0.5))
loss_fn = nn.CrossEntropyLoss()
X_tr = torch.randn(8, 4)
y_tr = torch.randint(0, 2, (8,))
model.eval()
with torch.no_grad():
    # same mode as validation
    train_eval = loss_fn(model(X_tr), y_tr)
model.train()
