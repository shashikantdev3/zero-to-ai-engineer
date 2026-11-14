"""Zero to AI Engineer · Evaluation · Part 3 of 11
Slide: Two judges, one answer
Run: python 01_two_judges_one_answer.py
"""
def judge(q, answer, reference=None,
          context=None):
    # toy grader: checks answer vs a target
    target = reference or context
    return answer.lower() in target.lower()
q = "When does the shop open?"
gold = "It opens at 9am"
chunks = "Old page: opens at 10am"
answer = "opens at 10am"
correct = judge(q, answer, reference=gold)
grounded = judge(q, answer, context=chunks)
print(correct, grounded)
