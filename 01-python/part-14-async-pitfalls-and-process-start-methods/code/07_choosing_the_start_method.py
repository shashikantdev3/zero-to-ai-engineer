"""Zero to AI Engineer · Python · Part 14 of 25
Slide: Choosing the start method
Run: python 07_choosing_the_start_method.py
"""
import multiprocessing as mp

# module level, so it can be pickled
def square(x: int) -> int:
    return x * x

# required for spawn and forkserver
if __name__ == "__main__":
    ctx = mp.get_context("spawn")
    with ctx.Pool(4) as pool:
        print(pool.map(square, range(8)))
