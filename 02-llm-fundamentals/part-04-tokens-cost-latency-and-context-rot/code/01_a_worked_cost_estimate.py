"""Zero to AI Engineer · LLM Fundamentals · Part 4 of 18
Slide: A worked cost estimate
Run: python 01_a_worked_cost_estimate.py
"""
reqs, tin, tout = 10_000, 1_500, 300
# illustrative prices, check the price sheet
p_in = 2.50 / 1e6
p_out = 10.00 / 1e6
per_req = tin * p_in + tout * p_out
daily = reqs * per_req
monthly = daily * 30
print(round(daily, 2), round(monthly, 2))
