"""Zero to AI Engineer · Python · Part 18 of 25
Slide: A property: chunking loses nothing
Run: python 06_a_property_chunking_loses_nothing.py
"""
# Needs: pip install hypothesis
from hypothesis import given
from hypothesis import strategies as st

def chunk_text(s: str, n: int) -> list[str]:
    return [s[i:i + n]
            for i in range(0, len(s), n)]

@given(st.text(),
       st.integers(min_value=1, max_value=50))
def test_chunking_loses_nothing(s, n):
    assert "".join(chunk_text(s, n)) == s
