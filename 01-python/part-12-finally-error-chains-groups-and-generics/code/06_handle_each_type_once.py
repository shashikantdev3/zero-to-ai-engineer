"""Zero to AI Engineer · Python · Part 12 of 25
Slide: Handle each type once
Run: python 06_handle_each_type_once.py
"""
# --- repeated from 05_build_the_exception_group.py so this file runs on its own ---
def validate(batch):
    errors = []
    for i, item in enumerate(batch):
        if "id" not in item:
            msg = f"item {i}: missing id"
            errors.append(ValueError(msg))
        elif item.get("ttl", 0) < 0:
            msg = f"item {i}: bad ttl"
            errors.append(TypeError(msg))
    if errors:
        raise ExceptionGroup(
            "batch validation failed", errors)

# --- this slide ---
batch = [{"x": 1}, {"id": 2, "ttl": -1}]
try:
    validate(batch)
except* ValueError as eg:
    print("missing:",
          [str(e) for e in eg.exceptions])
except* TypeError as eg:
    print("bad type:",
          [str(e) for e in eg.exceptions])
