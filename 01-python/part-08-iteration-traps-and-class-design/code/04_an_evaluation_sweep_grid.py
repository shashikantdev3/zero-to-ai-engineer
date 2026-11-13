"""Zero to AI Engineer · Python · Part 8 of 25
Slide: An evaluation sweep grid
Run: python 04_an_evaluation_sweep_grid.py
"""
from itertools import product, combinations

models = ["small", "large"]
temps = [0.0, 0.7]
prompts = ["v1", "v2", "v3"]
grid = list(product(models, temps, prompts))
print(len(grid))  # 12
items = ["a", "b", "c", "d"]
pairs = list(combinations(items, 2))
print(len(pairs))  # 6
