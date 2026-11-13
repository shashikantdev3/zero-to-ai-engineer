"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 13 of 28
Slide: Watch the distance ratio climb
Run: python 04_watch_the_distance_ratio_climb.py
"""
# Needs: pip install numpy
import numpy as np
rng = np.random.default_rng(0)
for d in (2, 10, 100, 1000):
    X = rng.random((1000, d))
    gaps = X - X[0]
    dist = np.linalg.norm(gaps, axis=1)[1:]
    # ratio climbs towards 1 as d grows
    print(d, dist.min() / dist.max())
