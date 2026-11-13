# Python · Part 7 of 25: Caches, Dispatch and Python Iteration

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Hand-written memoise versus lru_cache, and what neither fixes
2. functools.singledispatch
3. Question drill: decorators
4. Iterable versus iterator
5. Generators, yield from and itertools
6. Generator protocol: send, throw, close and the return value

## Key takeaways

- lru_cache: bounded, but no lists, no expiry
- singledispatch: first argument's type decides
- Decorators run at import; order matters
- Iterators and generators are single pass
- Lazy, constant memory; sort before groupby
- Prime, then send, throw, close

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_caching_an_embedding_call.py` | Caching an embedding call | yes |
| `code/02_a_default_and_a_list_version.py` | A default and a list version | yes |
| `code/03_a_dict_version_then_a_call.py` | A dict version, then a call | yes |
| `code/04_a_countdown_that_runs_once.py` | A countdown that runs once | yes |
| `code/05_lab_one_pass_or_two.py` | One pass or two | yes |
| `code/06_reading_a_file_lazily.py` | Reading a file lazily | yes |
| `code/07_batches_and_a_tree_walk.py` | Batches and a tree walk | yes |
| `code/08_a_running_mean_you_feed.py` | A running mean you feed | yes |
| `code/09_a_return_value_via_yield_from.py` | A return value via yield from | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/05_lab_one_pass_or_two.py` prints:

```text
list: 6 6
gen: 12 0
same object: True
next: 1 2
fresh: [1, 2, 3]
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. What happens when you pass a list to a function wrapped in L R U cache?**

- A. It skips the cache and runs
- B. It raises a type error
- C. It caches the list like a tuple

<details><summary>Answer</summary>

**B. It raises a type error**. Lists are unhashable: convert to a tuple first

</details>

**2. When you call render with two arguments, a and b, what decides which version runs?**

- A. The type of the last argument
- B. The types of both a and b
- C. Only the type of a

<details><summary>Answer</summary>

**C. Only the type of a**. Only the first argument's type decides

</details>

**3. The route decorator sits nearest the function, with the login check above it. What happens?**

- A. Login runs before every request
- B. Python refuses to import it
- C. Authentication is skipped

<details><summary>Answer</summary>

**C. Authentication is skipped**. Route registers the unprotected function

</details>

**4. You count items from a generator, then loop over it again for results, and get nothing. Why?**

- A. The first pass exhausted it
- B. Counting changed the items
- C. Generators reset only after close

<details><summary>Answer</summary>

**A. The first pass exhausted it**. Generators are single pass; use a list

</details>

**5. You use group by from iter tools, and one category appears twice. Why?**

- A. It only groups items next to each other
- B. The keys were not strings
- C. It drops keys after the first group

<details><summary>Answer</summary>

**A. It only groups items next to each other**. Sort by the key before groupby

</details>

**6. What happens if you call send with ten on a brand new generator?**

- A. It quietly ignores the ten
- B. It raises a type error
- C. It returns ten straight away

<details><summary>Answer</summary>

**B. It raises a type error**. Prime with next before the first send

</details>

## Say it in the interview

**Say it in the interview**

- Hand-written: ignores keywords, grows forever
- Check cache_info before trusting a cache
- Need expiry or sharing? Use Redis with TTL

**Say it in the interview**

- Type dispatch without editing the classes
- A default plus one function per type
- The limit: first argument only

**Say it in the interview**

- Iterable: loopable. Iterator: the cursor.
- Generators and files are single pass
- Two passes? Materialise into a list

**Say it in the interview**

- Freeze at yield: constant memory
- LLM token streaming is an async generator
- islice, chain, groupby (sorted), batched

**Say it in the interview**

- A generator is a two-way channel
- Prime first; throw and close for control
- Generators are where asyncio began

## Homework

- [ ] Print cache_info() after two identical calls
- [ ] Trigger the list TypeError, then fix it
- [ ] Write singledispatch for int and str
- [ ] Send to an unprimed generator, read the error
