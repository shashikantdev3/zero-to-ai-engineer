"""Zero to AI Engineer · Production and LLMOps · Part 1 of 38
Slide: A monthly cost function
Run: python 01_a_monthly_cost_function.py
"""
def monthly_cost(convs, turns, in_tok,
                 out_tok, in_p, out_p,
                 reason_tok=0, days=30):
    # reasoning tokens bill as output
    billed_out = out_tok + reason_tok
    in_cost = in_tok * in_p
    out_cost = billed_out * out_p
    per_call = (in_cost + out_cost) / 1e6
    return convs * turns * per_call * days
args = (10_000, 4, 2_000, 300, 1.0, 4.0)
print(monthly_cost(*args))
print(monthly_cost(*args, reason_tok=1_200))
