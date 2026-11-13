"""Zero to AI Engineer · Python · Part 23 of 25
Slide: chunk: route blocks by type
Run: python 03_chunk_route_blocks_by_type.py
"""
def chunk(blocks, mx=2000):
    out, paras = [], []
    for kind, t in blocks:
        if kind != "table":
            paras += split_para(t, mx)
            continue
        # flush, then the table on its own
        out += pack(paras, mx)
        paras = []
        out += split_table(t, mx)
    return out + pack(paras, mx)
