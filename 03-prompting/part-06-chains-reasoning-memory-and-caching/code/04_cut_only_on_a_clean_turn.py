"""Zero to AI Engineer · Prompting · Part 6 of 10
Slide: Cut only on a clean turn
Run: python 04_cut_only_on_a_clean_turn.py
"""
def is_tool_result(m):
    c = m.get("content")
    return isinstance(c, list) and any(
        b.get("type") == "tool_result"
        for b in c if isinstance(b, dict))
def safe_cut(h, keep_last):
    cut = max(0, len(h) - keep_last)
    while cut > 0 and (
            h[cut]["role"] != "user"
            or is_tool_result(h[cut])):
        cut -= 1
    return cut
