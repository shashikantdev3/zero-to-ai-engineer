"""Zero to AI Engineer · Python · Part 23 of 25
Slide: split_table: repeat the header
Run: python 05_split_table_repeat_the_header.py
"""
def split_table(t: str, mx: int) -> list[str]:
    lines = t.splitlines()
    head, rows = lines[:2], lines[2:]
    out, cur = [], []
    n = base = len("\n".join(head))
    for row in rows:
        if cur and n + len(row) + 1 > mx:
            out.append("\n".join(head + cur))
            cur, n = [], base
        cur.append(row)
        n += len(row) + 1
    return out + ["\n".join(head + cur)]
