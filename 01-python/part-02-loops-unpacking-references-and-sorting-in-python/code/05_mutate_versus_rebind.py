"""Zero to AI Engineer · Python · Part 2 of 25
Slide: Mutate Versus Rebind
Run: python 05_mutate_versus_rebind.py
"""
def mutate(xs):
    # caller sees this
    xs.append(4)

def rebind(xs):
    # only the local name moves
    xs = [99]

a = [1, 2, 3]
mutate(a)
rebind(a)
print(a)  # [1, 2, 3, 4]
