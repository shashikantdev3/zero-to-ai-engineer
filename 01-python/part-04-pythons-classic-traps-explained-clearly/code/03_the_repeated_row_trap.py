"""Zero to AI Engineer · Python · Part 4 of 25
Slide: The Repeated Row Trap
Run: python 03_the_repeated_row_trap.py
"""
# one inner list, repeated three times
bad = [[0] * 3] * 3
bad[0][0] = 1
print(bad)
# a fresh inner list for every row
grid = [[0] * 3 for _ in range(3)]
grid[0][0] = 1
print(grid)
