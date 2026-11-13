"""Zero to AI Engineer · Python · Part 5 of 25
Slide: Scoring, tools and folding
Run: python 03_scoring_tools_and_folding.py
"""
from functools import partial, reduce
def score(answer, expected, *, mode):
    if mode == "exact":
        return answer == expected
    return expected in answer
exact = partial(score, mode="exact")
TOOLS = {"lookup":
         lambda q: f"looked up {q}"}
print(TOOLS["lookup"]("disk"))
print(exact("a", "a"))
print(reduce(lambda acc, x: acc * x,
             [1, 2, 3, 4], 1))
