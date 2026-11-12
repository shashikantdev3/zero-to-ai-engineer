# Python · Part 4 of 25: Python's Classic Traps, Explained Clearly

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. is versus == and integer interning
2. Shallow versus deep copy
3. Modifying a collection while iterating it
4. += on a tuple that holds a list
5. Chained comparisons
6. Question drill: classic traps

## Key takeaways

- is for identity and singletons, == for values
- Shallow shares insides; deep copies the tree
- Dicts raise; lists skip silently
- Tuple += raises and still mutates
- Every comparison chains, even in and is
- Definition-time binding; copies shallow by default

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_is_versus_in_code.py` | is Versus == in Code | yes |
| `code/02_snapshot_an_agent_state.py` | Snapshot an Agent State | yes |
| `code/03_the_repeated_row_trap.py` | The Repeated Row Trap | yes |
| `code/04_deleting_dict_keys_safely.py` | Deleting Dict Keys Safely | yes |
| `code/05_the_silent_list_skip.py` | The Silent List Skip | yes |
| `code/06_lab_see_both_failures_yourself.py` | See Both Failures Yourself | yes |
| `code/07_watch_the_error_and_the_change.py` | Watch the Error and the Change | yes |
| `code/08_chains_versus_brackets.py` | Chains Versus Brackets | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/06_lab_see_both_failures_yourself.py` prints:

```text
dict raised RuntimeError
list result: [1, 2, 3]
comprehension: [2, 3]
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. What does the is operator actually check?**

- A. Whether two names share one object
- B. A faster version of double equals
- C. Whether two values share a type

<details><summary>Answer</summary>

**A. Whether two names share one object**. is checks identity, it is not a faster ==

</details>

**2. You snapshot a state with dict dot copy, then append to a nested list in the original. What happens to the snapshot?**

- A. It stays exactly the same
- B. It changes too
- C. Python raises an error

<details><summary>Answer</summary>

**B. It changes too**. dict.copy() copies the outside only

</details>

**3. What happens when you remove items from a list while looping over it?**

- A. Every match is removed correctly
- B. Python raises a RuntimeError
- C. Some items are skipped, with no error

<details><summary>Answer</summary>

**C. Some items are skipped, with no error**. Lists fail silently; dicts and sets raise

</details>

**4. A tuple holds one and a list with two. After += adds three to that list and raises a TypeError, what does the list hold?**

- A. Two and three
- B. Nothing, the list is gone
- C. Only two

<details><summary>Answer</summary>

**A. Two and three**. The extend runs before the error

</details>

**5. What does one less than three greater than two evaluate to?**

- A. False
- B. True
- C. An error

<details><summary>Answer</summary>

**B. True**. 1 < 3 > 2 means (1 < 3) and (3 > 2)

</details>

**6. When += on a list inside a tuple fails, what really happened?**

- A. No error, the list just changed
- B. A TypeError, and nothing changed
- C. A TypeError, and the list changed

<details><summary>Answer</summary>

**C. A TypeError, and the list changed**. Both: the error and the mutation

</details>

## Say it in the interview

**Say It in the Interview**

- is only for None, True, False, sentinels
- Relying on the small-int cache is a bug

**Say It in the Interview**

- Shallow: new container, same inner objects
- Deep: whole tree, slower, can fail
- For state, prefer immutable updates

**Say It in the Interview**

- Dicts fail loud, lists fail silent
- Prefer a comprehension: no shared mutation

**Say It in the Interview**

- Exception raised, list still changed
- Use extend: no assignment step

**Say It in the Interview**

- Chains read like maths, x read once
- Bracket any chain mixing == and in

## Homework

- [ ] Compare two int("1000") with == and is
- [ ] Mutate a nested dict after copy and deepcopy
- [ ] Run t[1] += [3], then print t
- [ ] Rewrite a removing loop as a comprehension
