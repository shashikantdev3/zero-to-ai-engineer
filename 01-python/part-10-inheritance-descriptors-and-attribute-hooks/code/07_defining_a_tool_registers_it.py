"""Zero to AI Engineer · Python · Part 10 of 25
Slide: Defining a tool registers it
Run: python 07_defining_a_tool_registers_it.py
"""
# --- repeated from 06_a_self_registering_base_class.py so this file runs on its own ---
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

# --- this slide ---
class SearchTool(Tool, name="search"):
    def run(self, q: str) -> str:
        return q

print(Tool.registry)
# {'search': <class '__main__.SearchTool'>}
