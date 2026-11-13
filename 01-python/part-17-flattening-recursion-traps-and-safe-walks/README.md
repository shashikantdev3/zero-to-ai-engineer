# Python · Part 17 of 25: Flattening, Recursion Traps and Safe Walks

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Flattening with lists, and unflattening
2. Flatten a nested list, and the string trap
3. Small recursive helpers: deep sum, deep merge and a cycle guard
4. sys.setrecursionlimit is a smell, and why there is no tail-call optimisation
5. Question drill: data structures and recursion

## Key takeaways

- Index keys; collisions break the round trip
- Test for list, not iterable
- Exclude bool, state policy, guard cycles
- Explicit stack beats a higher limit
- Know the one-line answer to each trap

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_flatten_with_index_keys.py` | Flatten with index keys | yes |
| `code/02_unflatten_walks_or_creates_dicts.py` | Unflatten walks or creates dicts | yes |
| `code/03_flatten_a_nested_list_lazily.py` | Flatten a nested list lazily | yes |
| `code/04_lab_list_versus_iterable_side_by_side.py` | List versus Iterable, side by side | yes |
| `code/05_deep_sum_that_skips_booleans.py` | Deep sum that skips booleans | yes |
| `code/06_deep_merge_with_a_stated_policy.py` | Deep merge with a stated policy | yes |
| `code/07_a_walk_with_a_cycle_guard.py` | A walk with a cycle guard | yes |
| `code/08_checking_the_recursion_limit.py` | Checking the recursion limit | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/04_lab_list_versus_iterable_side_by_side.py` prints:

```text
[1, 2, 3, 'ab']
first: 1
Iterable: RecursionError
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. Does unflatten always give back exactly what you flattened?**

- A. No, keys with dots collide
- B. Only when the input has lists
- C. Yes, it is an exact inverse

<details><summary>Answer</summary>

**A. No, keys with dots collide**. Separator collisions and lists break the round trip

</details>

**2. If your flatten recurses into anything iterable, what happens to the string ab?**

- A. It stays whole as ab
- B. It recurses until a RecursionError
- C. It splits cleanly into a and b

<details><summary>Answer</summary>

**B. It recurses until a RecursionError**. Strings iterate to themselves; test for list

</details>

**3. A naive deep sum that adds every int meets a dict holding ok set to True. What does it return?**

- A. One, because bool is an int
- B. Zero, booleans are skipped
- C. An error, True is not a number

<details><summary>Answer</summary>

**A. One, because bool is an int**. True sums to one unless you exclude bool

</details>

**4. If you write a function tail-recursively, does Python stop adding frames?**

- A. Only once the limit is reached
- B. No, every call still adds a frame
- C. Yes, Python optimises tail calls

<details><summary>Answer</summary>

**B. No, every call still adds a frame**. Tail recursion still costs one frame per call

</details>

**5. Your recursive function hits the limit on deep input. Is raising the recursion limit the right fix?**

- A. Yes, if you set it high enough
- B. Yes, once it is tail-recursive
- C. No, it can crash the interpreter

<details><summary>Answer</summary>

**C. No, it can crash the interpreter**. Use an explicit stack, not a higher limit

</details>

## Say it in the interview

**Flattening lists, in the interview**

- A list is a dict keyed by index.
- Guard empty input, and ask the consumer.
- Reject separator keys, or keep tuple paths.

**Flattening lists, in the interview**

- A lazy generator with yield from.
- Test for list, not iterable.
- Linear time; stack depth equals nesting.

**Recursive helpers, in the interview**

- True is an int; exclude bool.
- State the merge conflict policy.
- Guard cycles with visited object ids.

**The recursion limit, in the interview**

- The limit protects the C stack.
- No tail calls; tracebacks matter more.
- Unbounded depth gets an explicit stack.

## Homework

- [ ] Write flatten with index keys and guard
- [ ] Make two different keys collide
- [ ] Test deep sum with and without bool
- [ ] Rewrite depth as a loop
