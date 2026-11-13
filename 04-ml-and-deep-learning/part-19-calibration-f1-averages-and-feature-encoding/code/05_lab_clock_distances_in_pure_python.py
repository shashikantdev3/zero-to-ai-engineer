"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 19 of 28
Follow-along lab: Clock distances in pure Python
Run: python 05_lab_clock_distances_in_pure_python.py
"""
import math
def circle(h):
    a = 2 * math.pi * h / 24
    return (math.sin(a), math.cos(a))
near = math.dist(circle(23), circle(0))
far = math.dist(circle(12), circle(0))
print("raw gap 23 to 0:", 23 - 0)
print(f"circle gap 23 to 0: {near:.3f}")
print(f"circle gap 12 to 0: {far:.3f}")
s3, c3 = circle(3)
s9, c9 = circle(9)
print(f"sin 3h, 9h: {s3:.3f} {s9:.3f}")
print(f"cos 3h, 9h: {c3:.3f} {c9:.3f}")
