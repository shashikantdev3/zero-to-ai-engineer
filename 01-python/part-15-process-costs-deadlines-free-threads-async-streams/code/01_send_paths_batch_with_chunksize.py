"""Zero to AI Engineer · Python · Part 15 of 25
Slide: Send Paths, Batch With Chunksize
Run: python 01_send_paths_batch_with_chunksize.py
"""
# Note: this reads files that you supply. Without them it stops with FileNotFoundError.
from concurrent.futures import (
    ProcessPoolExecutor)
# send a path, not file contents
def parse(path: str) -> int:
    with open(path, encoding="utf-8") as f:
        return sum(1 for _ in f)
if __name__ == "__main__":
    paths = ["a.txt", "b.txt"]
    with ProcessPoolExecutor() as ex:
        counts = list(ex.map(
            parse, paths, chunksize=16))
    # a lambda here fails: cannot be pickled
