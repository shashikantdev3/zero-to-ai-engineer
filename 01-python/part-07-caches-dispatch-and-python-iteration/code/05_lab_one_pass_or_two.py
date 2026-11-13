"""Zero to AI Engineer · Python · Part 7 of 25
Follow-along lab: One pass or two
Run: python 05_lab_one_pass_or_two.py
"""
def doubled(xs):
    for x in xs:
        yield x * 2

nums = [1, 2, 3]
print("list:", sum(nums), sum(nums))
gen = doubled(nums)
print("gen:", sum(gen), sum(gen))
print("same object:", iter(gen) is gen)
it = iter(nums)
print("next:", next(it), next(it))
print("fresh:", list(iter(nums)))
