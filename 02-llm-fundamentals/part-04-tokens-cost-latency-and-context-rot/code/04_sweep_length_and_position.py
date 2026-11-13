"""Zero to AI Engineer · LLM Fundamentals · Part 4 of 18
Slide: Sweep length and position
Run: python 04_sweep_length_and_position.py
"""
gold = ["G1", "G2", "G3"]
fill = [f"D{i}" for i in range(100)]
def run_eval(ctx):
    # stand-in for your real multi-hop eval
    return len(ctx)
for n in (5, 20, 50, 100):
    f = fill[: n - len(gold)]
    spots = {"start": 0, "mid": len(f) // 2,
             "end": len(f)}
    for pos, i in spots.items():
        ctx = f[:i] + gold + f[i:]
        print(n, pos, run_eval(ctx))
