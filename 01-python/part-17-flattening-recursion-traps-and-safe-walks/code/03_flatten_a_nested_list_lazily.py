"""Zero to AI Engineer · Python · Part 17 of 25
Slide: Flatten a nested list lazily
Run: python 03_flatten_a_nested_list_lazily.py
"""
def flatten_list(lst):
    for item in lst:
        # test for list, not "is iterable"
        if isinstance(item, list):
            yield from flatten_list(item)
        else:
            yield item

nested = [1, [2, [3, "ab"]], []]
print(list(flatten_list(nested)))
# [1, 2, 3, 'ab']
