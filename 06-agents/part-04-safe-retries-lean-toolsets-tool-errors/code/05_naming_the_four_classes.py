"""Zero to AI Engineer · Agents and Tools · Part 4 of 26
Slide: Naming the four classes
Run: python 05_naming_the_four_classes.py
"""
from enum import Enum

class Kind(Enum):
    TRANSIENT = "transient"
    SEMANTIC = "semantic"
    PERMANENT = "permanent"
    SYSTEMIC = "systemic"

# None stands for a timeout
RETRY = (408, 429, 502, 503, 504, None)
