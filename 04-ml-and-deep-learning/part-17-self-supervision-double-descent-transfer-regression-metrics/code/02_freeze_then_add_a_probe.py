"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 17 of 28
Slide: Freeze, Then Add a Probe
Run: python 02_freeze_then_add_a_probe.py
"""
# Needs: pip install torch
import torch.nn as nn
hidden_size, num_classes = 16, 3
# a tiny stand-in for a pretrained model
backbone = nn.Sequential(
    nn.Linear(8, hidden_size), nn.ReLU()
)
for p in backbone.parameters():
    # freeze the pretrained model
    p.requires_grad = False
# linear probe: the only trainable part
head = nn.Linear(hidden_size, num_classes)
# optimise only head.parameters()
