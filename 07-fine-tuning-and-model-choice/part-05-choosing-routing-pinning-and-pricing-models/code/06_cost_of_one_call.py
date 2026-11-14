"""Zero to AI Engineer · Fine-tuning and Model Choice · Part 5 of 10
Slide: Cost of one call
Run: python 06_cost_of_one_call.py
"""
# prices are per one million tokens
def cost(tin, tout, p_in, p_out):
    in_cost = tin * p_in / 1e6
    out_cost = tout * p_out / 1e6
    return in_cost + out_cost

# illustrative prices only
print(cost(2000, 300, 0.15, 0.60))
