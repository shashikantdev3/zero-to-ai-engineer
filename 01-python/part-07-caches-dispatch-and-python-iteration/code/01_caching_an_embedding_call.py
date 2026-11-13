"""Zero to AI Engineer · Python · Part 7 of 25
Slide: Caching an embedding call
Run: python 01_caching_an_embedding_call.py
"""
from functools import lru_cache

@lru_cache(maxsize=1024)
def embed(text: str) -> tuple[float, ...]:
    # stands in for a real call
    return (float(len(text)),)

embed("hi"); embed("hi")
print(embed.cache_info())
embed.cache_clear()
# embed(["hi"]) -> TypeError: unhashable
