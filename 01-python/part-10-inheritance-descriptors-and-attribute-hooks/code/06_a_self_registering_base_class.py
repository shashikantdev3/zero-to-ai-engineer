"""Zero to AI Engineer · Python · Part 10 of 25
Slide: A self registering base class
Run: python 06_a_self_registering_base_class.py
"""
class Tool:
    registry: dict[str, type] = {}
    def __init_subclass__(cls, /,
                          name=None, **kw):
        super().__init_subclass__(**kw)
        if "run" not in cls.__dict__:
            m = f"{cls.__name__} needs run()"
            raise TypeError(m)
        key = name or cls.__name__
        Tool.registry[key] = cls
