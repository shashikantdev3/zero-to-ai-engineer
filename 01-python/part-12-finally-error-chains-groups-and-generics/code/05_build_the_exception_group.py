"""Zero to AI Engineer · Python · Part 12 of 25
Slide: Build the exception group
Run: python 05_build_the_exception_group.py
"""
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
