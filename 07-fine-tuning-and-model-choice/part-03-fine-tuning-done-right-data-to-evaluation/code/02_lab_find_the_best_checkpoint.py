"""Zero to AI Engineer · Fine-tuning and Model Choice · Part 3 of 10
Follow-along lab: Find the Best Checkpoint
Run: python 02_lab_find_the_best_checkpoint.py
"""
steps = [50, 100, 150, 200, 250, 300]
train = [2.1, 1.6, 1.2, 0.9, 0.6, 0.4]
val = [2.2, 1.8, 1.5, 1.4, 1.6, 1.9]
best = val.index(min(val))
print("last ckpt:", steps[-1], val[-1])
print("best ckpt:", steps[best], val[best])
for i in range(1, len(val)):
    if val[i] > val[i - 1]:
        print("overfit from step", steps[i])
        break
gap = round(val[-1] - train[-1], 2)
print("final gap:", gap)
