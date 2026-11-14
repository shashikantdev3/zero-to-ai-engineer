"""Zero to AI Engineer · Agents and Tools · Part 25 of 26
Slide: Tests: step cap and unknown node
Run: python 08_tests_step_cap_and_unknown_node.py
"""
def test_step_limit():
    # state changes each step, so no cycle
    edges = {"inc": lambda s: "inc"}
    with pytest.raises(StepLimit):
        run({"inc": inc}, edges, "inc",
            {"n": 0}, cap=5)

def test_unknown_node():
    edges = {"a": lambda s: "missing"}
    with pytest.raises(UnknownNode):
        run({"a": lambda s: {"x": 2}}, edges,
            "a", {"x": 1})
