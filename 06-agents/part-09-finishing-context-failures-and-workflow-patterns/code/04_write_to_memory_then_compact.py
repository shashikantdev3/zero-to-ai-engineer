"""Zero to AI Engineer · Agents and Tools · Part 9 of 26
Slide: Write to memory, then compact
Run: python 04_write_to_memory_then_compact.py
"""
COMPACT_AT = 50
memory = {}

def before_call(tenant, user, msgs):
    clear_old(msgs)
    if len(str(msgs)) > COMPACT_AT:
        # write facts before compacting
        memory[(tenant, user)] = "error E42"
        # lossy summary replaces history
        msgs = [{"role": "user",
                 "content": "summary"}]
    return msgs
