"""Zero to AI Engineer · Python · Interview Quiz
Slide: Copying a nested state
Run: python 10_copying_a_nested_state.py
"""
import copy
state = {"msgs": ["hi"]}
shallow = state.copy()
deep = copy.deepcopy(state)
state["msgs"].append("hello")
print(len(shallow["msgs"]), len(deep["msgs"]))
