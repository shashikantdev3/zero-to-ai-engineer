"""Zero to AI Engineer · Agents and Tools · Part 5 of 26
Slide: A short index plus describe_tool
Run: python 04_a_short_index_plus_describe_tool.py
"""
# level 1: names and short descriptions
INDEX = {"get_logs": "Read service logs",
         "restart": "Restart one service"}
# full schemas stay out until asked for
FULL = {"get_logs": {"required": ["svc"]},
        "restart": {"required": ["svc"]}}
def describe_tool(name):
    return FULL[name]
# fixed order keeps the cached prefix
lines = [f"{n}: {INDEX[n]}" for n in INDEX]
prompt = "\n".join(lines)
print(describe_tool("restart"))
