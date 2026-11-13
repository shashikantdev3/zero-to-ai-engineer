"""Zero to AI Engineer · Python · Part 6 of 25
Slide: A Registry Decorator
Run: python 06_a_registry_decorator.py
"""
TOOLS = {}
def tool(name):
    # runs at import
    print(f"registering {name}")
    def deco(fn):
        TOOLS[name] = fn
        return fn
    return deco
# prints as soon as the module loads
@tool("search")
def search(q: str) -> str:
    return f"results for {q}"
