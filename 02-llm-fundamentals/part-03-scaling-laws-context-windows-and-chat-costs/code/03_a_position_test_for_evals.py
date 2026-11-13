"""Zero to AI Engineer · LLM Fundamentals · Part 3 of 18
Slide: A position test for evals
Run: python 03_a_position_test_for_evals.py
"""
def place_gold_chunk(docs, gold, pos):
    i = {"start": 0, "end": len(docs),
         "middle": len(docs) // 2}[pos]
    return docs[:i] + [gold] + docs[i:]

def run_eval(questions, ctx):
    # stub: a real eval scores model answers
    return ctx.index("GOLD")
docs, gold = ["d1", "d2", "d3", "d4"], "GOLD"
for pos in ["start", "middle", "end"]:
    ctx = place_gold_chunk(docs, gold, pos)
    print(pos, run_eval([], ctx))
