"""Zero to AI Engineer · Python · Part 5 of 25
Slide: A counter with nonlocal
Run: python 02_a_counter_with_nonlocal.py
"""
def make_counter():
    count = 0
    def inc():
        nonlocal count
        count += 1
        return count
    return inc
c = make_counter(); c(); assert c() == 2

total = 0
def bad():
    total += 1  # UnboundLocalError
