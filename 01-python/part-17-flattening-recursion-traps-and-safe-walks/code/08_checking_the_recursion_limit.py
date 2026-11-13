"""Zero to AI Engineer · Python · Part 17 of 25
Slide: Checking the recursion limit
Run: python 08_checking_the_recursion_limit.py
"""
import sys
print(sys.getrecursionlimit())  # 1000

def depth(n: int) -> int:
    return 0 if n == 0 else 1 + depth(n - 1)

# depth(5000) raises RecursionError.
# Prefer a loop or an explicit stack
# over raising the limit.
