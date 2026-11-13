"""Zero to AI Engineer · Python · Part 12 of 25
Slide: A generic function and class
Run: python 07_a_generic_function_and_class.py
"""
def first[T](items: list[T]) -> T:
    return items[0]

class Cache[K, V]:
    def __init__(self) -> None:
        self._d: dict[K, V] = {}
    def get(self, key: K) -> V | None:
        return self._d.get(key)
