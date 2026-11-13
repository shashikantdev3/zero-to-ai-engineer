"""Zero to AI Engineer · Python · Part 12 of 25
Slide: A bound and a recursive alias
Run: python 08_a_bound_and_a_recursive_alias.py
"""
# bound: S must be a str
def longest[S: str](a: S, b: S) -> S:
    return a if len(a) >= len(b) else b

type JSON = (
    dict[str, JSON] | list[JSON]
    | str | int | float | bool | None
)
