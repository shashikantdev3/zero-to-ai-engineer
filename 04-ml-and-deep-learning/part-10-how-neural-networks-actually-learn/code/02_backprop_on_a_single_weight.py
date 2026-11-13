"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 10 of 28
Slide: Backprop on a single weight
Run: python 02_backprop_on_a_single_weight.py
"""
# Needs: pip install torch
import torch
w = torch.tensor(2.0, requires_grad=True)
x, y = torch.tensor(3.0), torch.tensor(10.0)
loss = (w * x - y) ** 2
loss.backward()
# d/dw (wx - y)^2 = 2(wx - y)x
# = 2(6 - 10)(3) = -24
print(w.grad)
# inference: no graph, less memory
with torch.no_grad():
    pred = w * x
print(pred.requires_grad)
