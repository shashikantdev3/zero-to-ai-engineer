"""Zero to AI Engineer · Python · Part 7 of 25
Slide: A running mean you feed
Run: python 08_a_running_mean_you_feed.py
"""
def running_mean():
    total, n, mean = 0.0, 0, None
    while True:
        x = yield mean
        total, n = total + x, n + 1
        mean = total / n

g = running_mean()
next(g)  # prime
print(g.send(10))  # 10.0
print(g.send(20))  # 15.0
g.close()
