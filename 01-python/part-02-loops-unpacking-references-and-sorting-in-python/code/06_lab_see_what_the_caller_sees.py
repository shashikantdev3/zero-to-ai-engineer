"""Zero to AI Engineer · Python · Part 2 of 25
Follow-along lab: See What the Caller Sees
Run: python 06_lab_see_what_the_caller_sees.py
"""
def mutate(xs):
    xs.append(4)
def rebind(xs):
    xs = [99]
def bump(n):
    n += 1
a = [1, 2, 3]
mutate(a)
print("after mutate:", a)
rebind(a)
print("after rebind:", a)
k = 5
bump(k)
print("after bump:", k)
