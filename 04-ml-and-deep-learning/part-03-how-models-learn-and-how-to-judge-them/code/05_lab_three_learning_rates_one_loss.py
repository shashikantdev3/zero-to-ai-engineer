"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 3 of 28
Follow-along lab: Three Learning Rates, One Loss
Run: python 05_lab_three_learning_rates_one_loss.py
"""
# loss = (w - 3) ** 2, lowest at w = 3
def train(lr, steps=20):
    w = 0.0
    for _ in range(steps):
        grad = 2 * (w - 3)
        w = w - lr * grad
    return w

for lr in (0.01, 0.1, 1.1):
    w = train(lr)
    print(f"lr {lr}: w = {w:.2f}")
print("target: w = 3.00")
