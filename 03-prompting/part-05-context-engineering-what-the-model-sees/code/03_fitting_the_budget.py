"""Zero to AI Engineer · Prompting · Part 5 of 10
Slide: Fitting the Budget
Run: python 03_fitting_the_budget.py
"""
def fit(fixed, docs, budget, max_out):
    room = budget - max_out - n_tokens(fixed)
    kept, used = [], 0
    for d in docs:  # sorted, best first
        t = n_tokens(d)
        if used + t > room:
            break
        kept.append(d); used += t
    prompt = fixed + "\n" + "\n".join(kept)
    if n_tokens(prompt) + max_out > budget:
        raise BudgetExceeded("over budget")
    return prompt
