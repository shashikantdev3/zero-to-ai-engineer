"""Zero to AI Engineer · RAG and Vector Search · Part 13 of 26
Follow-along lab: Pull the cost levers yourself
Run: python 02_lab_pull_the_cost_levers_yourself.py
"""
def cost(k, hist, out):
    inp = 800 + k * 500 + hist + 50
    return (inp * 3 + out * 15) / 1_000_000

base = cost(10, 1200, 300)
print(f"base: {base:.5f}")
print(f"fewer chunks: {cost(5, 1200, 300):.5f}")
print(f"trim history: {cost(5, 400, 300):.5f}")
print(f"cap output: {cost(5, 400, 150):.5f}")
saved = 1 - cost(5, 400, 150) / base
print(f"saved: {saved:.0%}")
