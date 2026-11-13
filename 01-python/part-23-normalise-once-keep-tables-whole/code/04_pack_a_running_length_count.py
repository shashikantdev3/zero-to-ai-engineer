"""Zero to AI Engineer · Python · Part 23 of 25
Slide: pack: a running length count
Run: python 04_pack_a_running_length_count.py
"""
def pack(parts, mx):
    out, cur, n = [], [], 0
    for p in parts:
        add = len(p) + (1 if cur else 0)
        if cur and n + add > mx:
            out.append("\n".join(cur))
            cur, n, add = [], 0, len(p)
        cur.append(p)
        n += add
    if cur:
        out.append("\n".join(cur))
    return out
