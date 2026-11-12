# Python · Part 2 of 25: Loops, Unpacking, References and Sorting in Python

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Iteration built-ins: enumerate, zip, any, all, sorted with key
2. Unpacking, walrus and match
3. Pass by object reference
4. List, tuple and set: choosing by operation
5. sort versus sorted, itemgetter and multi-pass stable sorting

## Key takeaways

- Strict zip; all of empty is True
- Right dict wins; bare case name captures
- Mutation is shared, rebinding is local
- Pick the collection by operation
- sort returns None; stable passes mix orders

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_ranking_with_a_tuple_key.py` | Ranking with a Tuple Key | yes |
| `code/02_strict_zip_and_empty_checks.py` | Strict zip and Empty Checks | yes |
| `code/03_unpack_merge_read_in_blocks.py` | Unpack, Merge, Read in Blocks | yes |
| `code/04_match_on_tool_call_payloads.py` | match on Tool-Call Payloads | yes |
| `code/05_mutate_versus_rebind.py` | Mutate Versus Rebind | yes |
| `code/06_lab_see_what_the_caller_sees.py` | See What the Caller Sees | yes |
| `code/07_membership_dedup_and_tuple_keys.py` | Membership, Dedup and Tuple Keys | yes |
| `code/08_two_pass_stable_sort.py` | Two-Pass Stable Sort | yes |
| `code/09_the_none_trap.py` | The None Trap | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/06_lab_see_what_the_caller_sees.py` prints:

```text
after mutate: [1, 2, 3, 4]
after rebind: [1, 2, 3, 4]
after bump: 5
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. If your list of validation checks is empty, what does all of it return?**

- A. False
- B. True
- C. It raises an error

<details><summary>Answer</summary>

**B. True**. all of nothing is True; assert checks exist

</details>

**2. In a match statement, what does a case with only a bare name do?**

- A. Raises a syntax error
- B. Captures anything and always matches
- C. Compares against that variable's value

<details><summary>Answer</summary>

**B. Captures anything and always matches**. A bare name captures; use dotted names or guards

</details>

**3. A function sets its list parameter to a new list. What happens to the caller's list?**

- A. It becomes the new list
- B. It is emptied
- C. Nothing, it stays the same

<details><summary>Answer</summary>

**C. Nothing, it stays the same**. Rebinding moves a name; mutating changes the object

</details>

**4. Does a set keep its elements in insertion order, like a dict?**

- A. No, sets are unordered
- B. Yes, but only for strings
- C. Yes, exactly like a dict

<details><summary>Answer</summary>

**A. No, sets are unordered**. Dicts keep order; sets do not

</details>

**5. In pass two, with reverse set to True, what order do the two rows tied at 0.8 keep?**

- A. Their order from pass one
- B. No guaranteed order
- C. The opposite of pass one

<details><summary>Answer</summary>

**A. Their order from pass one**. reverse=True keeps stability

</details>

## Say it in the interview

**Iteration Built-ins**

- Strict zip: a dropped result raises
- all of an empty list is True
- Tuple key and stable sort: reproducible ranking

**Unpacking and match**

- Star for head and tail, right dict wins
- match beats chained isinstance checks
- Check the runtime version first

**Argument Passing**

- A reference to the same object, not a copy
- Mutation is shared; rebinding is local
- Return new structures; easier to test

**Choosing a Collection**

- Choose by the operation you need most
- List membership in a loop is quadratic
- A tuple is only as hashable as its contents

**Sorting**

- x = items.sort() leaves x as None
- itemgetter and attrgetter for multi-field keys
- Two stable passes beat negating a string

## Homework

- [ ] Run strict zip on mismatched lists
- [ ] Write match with a bare name case
- [ ] Swap a list membership check for a set
- [ ] Do a two-pass stable sort
