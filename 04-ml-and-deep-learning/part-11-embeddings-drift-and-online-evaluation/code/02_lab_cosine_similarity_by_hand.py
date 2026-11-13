"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 11 of 28
Follow-along lab: Cosine similarity by hand
Run: python 02_lab_cosine_similarity_by_hand.py
"""
import math
def cos(u, v):
    dot = sum(x * y for x, y in zip(u, v))
    nu = math.sqrt(sum(x * x for x in u))
    nv = math.sqrt(sum(y * y for y in v))
    return dot / (nu * nv)
cat = [1, 2, 0]
dog = [1, 1.8, 0.2]
car = [0, 0.1, 3]
print("cat~dog:", round(cos(cat, dog), 3))
print("cat~car:", round(cos(cat, car), 3))
cat2, dog2 = [2, 1, 1, 0], [1, 2, 0, 1]
print("model 2:", round(cos(cat2, dog2), 3))
