"""Zero to AI Engineer · Python · Part 1 of 25
Slide: A safe default for temperature
Run: python 03_a_safe_default_for_temperature.py
"""
def call(temperature: float | None = None):
    # wrong: temperature = temperature or 0.7  -> 0.0 becomes 0.7
    if temperature is None:
        temperature = 0.7
    return temperature

assert call(0.0) == 0.0
