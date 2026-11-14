"""Zero to AI Engineer · Fine-tuning and Model Choice · Part 6 of 10
Slide: Cost per ticket in code
Run: python 01_cost_per_ticket_in_code.py
"""
def cost_per_ticket(model, rate, human):
    # failed tickets go to a human
    return model + (1 - rate) * human

cheap = cost_per_ticket(0.003, 0.70, 2.0)
strong = cost_per_ticket(0.02, 0.90, 2.0)
print(round(cheap, 3), round(strong, 3))
print(round(cheap / strong, 1))
# illustrative numbers only
# reopens are not modelled: price them apart
