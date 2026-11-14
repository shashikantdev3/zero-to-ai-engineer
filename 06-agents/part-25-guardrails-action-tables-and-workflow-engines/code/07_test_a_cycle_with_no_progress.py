"""Zero to AI Engineer · Agents and Tools · Part 25 of 26
Slide: Test: a cycle with no progress
Run: python 07_test_a_cycle_with_no_progress.py
"""
idle = lambda s: {}

def test_no_progress_cycle():
    edges = {"a": lambda s: "b",
             "b": lambda s: "a"}
    with pytest.raises(CycleDetected):
        run({"a": idle, "b": idle}, edges,
            "a", {"x": 1})
