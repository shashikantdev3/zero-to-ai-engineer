"""Zero to AI Engineer · Agents and Tools · Part 9 of 26
Slide: Clearing old tool results
Run: python 03_clearing_old_tool_results.py
"""
msgs = [{"role": "tool", "id": "t1",
         "content": "x" * 3000}]
msgs += [{"role": "user", "content": "ok"}]*6

def clear_old(msgs):
    # keep the last six turns verbatim
    for m in msgs[:-6]:
        big = len(m["content"]) > 2_000
        if m["role"] == "tool" and big:
            stub = "cleared:" + m["id"]
            m["content"] = stub
