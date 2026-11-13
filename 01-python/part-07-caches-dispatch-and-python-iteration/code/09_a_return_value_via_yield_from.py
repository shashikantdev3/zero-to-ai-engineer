"""Zero to AI Engineer · Python · Part 7 of 25
Slide: A return value via yield from
Run: python 09_a_return_value_via_yield_from.py
"""
def sub():
    yield 1
    return "done"

def outer():
    result = yield from sub()
    yield result

print(list(outer()))
# [1, 'done']
