"""Zero to AI Engineer · Python · Part 23 of 25
Slide: split_para: sentences, then hard
Run: python 06_split_para_sentences_then_hard.py
"""
import re
def split_para(t: str, mx: int) -> list[str]:
    out, cur, n = [], [], 0
    for s in re.split(r"(?<=[.!?])(?=\s)", t):
        for i in range(0, len(s), mx):
            p = s[i:i + mx]
            if cur and n + len(p) > mx:
                out += ["".join(cur).strip()]
                cur, n = [], 0
            cur.append(p)
            n += len(p)
    return out + ["".join(cur).strip()]
