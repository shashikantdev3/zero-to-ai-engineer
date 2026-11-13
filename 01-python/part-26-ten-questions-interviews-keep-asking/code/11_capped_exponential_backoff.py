"""Zero to AI Engineer · Python · Interview Quiz
Slide: Capped exponential backoff
Run: python 11_capped_exponential_backoff.py
"""
def delays(base=0.5, cap=4.0, attempts=6):
    return [min(cap, base * 2 ** n)
            for n in range(attempts)]
print(delays())
