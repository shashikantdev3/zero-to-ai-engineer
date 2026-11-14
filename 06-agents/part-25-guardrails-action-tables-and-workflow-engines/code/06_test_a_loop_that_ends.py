"""Zero to AI Engineer · Agents and Tools · Part 25 of 26
Slide: Test: a loop that ends
Run: python 06_test_a_loop_that_ends.py
"""
# Needs: pip install pytest
import pytest

inc = lambda s: {"n": s["n"] + 1}
stop3 = lambda s: "inc" if s["n"] < 3 else END

def test_loop_terminates():
    out = run({"inc": inc}, {"inc": stop3},
              "inc", {"n": 0})
    assert out["n"] == 3
