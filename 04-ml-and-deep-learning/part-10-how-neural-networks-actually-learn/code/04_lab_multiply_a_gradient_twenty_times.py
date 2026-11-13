"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 10 of 28
Follow-along lab: Multiply a gradient twenty times
Run: python 04_lab_multiply_a_gradient_twenty_times.py
"""
def through(layers, local):
    grad = 1.0
    for _ in range(layers):
        grad *= local
    return grad

small = through(20, 0.5)
big = through(20, 1.5)
print(f"vanishing: {small:.7f}")
print(f"exploding: {big:.1f}")
print(f"clipped: {min(big, 1.0)}")
print(f"5 layers: {through(5, 0.5)}")
