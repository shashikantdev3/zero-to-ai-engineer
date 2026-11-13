"""Zero to AI Engineer · Python · Part 8 of 25
Slide: Subclassing str with __new__
Run: python 05_subclassing_str_with_new.py
"""
class Version(str):
    def __new__(cls, value: str):
        if not value.startswith("v"):
            value = "v" + value
        return super().__new__(cls, value)

print(Version("1.2"))
