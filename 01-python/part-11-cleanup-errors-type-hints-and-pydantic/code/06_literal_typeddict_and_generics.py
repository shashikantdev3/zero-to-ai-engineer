"""Zero to AI Engineer · Python · Part 11 of 25
Slide: Literal, TypedDict and Generics
Run: python 06_literal_typeddict_and_generics.py
"""
from typing import Literal, TypedDict
from typing import TypeVar, Callable
Route = Literal["small", "large"]
class ToolCall(TypedDict):
    name: str
    arguments: dict
T = TypeVar("T")
def first_or_none(items: list[T]) -> T | None:
    return items[0] if items else None
def run(fn: Callable[[], T]) -> T:
    return fn()
def pick(route: Route) -> str: return route
