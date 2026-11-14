"""Zero to AI Engineer · Agents and Tools · Part 17 of 26
Follow-along lab: Count and route MCP calls
Run: python 03_lab_count_and_route_mcp_calls.py
"""
apps, tools = 5, 8
print("custom:", apps * tools)
print("with MCP:", apps + tools)
owner = {"tools": "model",
         "resources": "application",
         "prompts": "user"}
calls = ["tools/call", "resources/read",
         "prompts/get"]
for m in calls:
    kind = m.split("/")[0]
    print(m, "->", owner[kind])
