# Python · Part 1 of 25: Names, Objects and the Core Language

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers


## Key takeaways

- Python orchestrates. Native code does the heavy maths.
- Names point at objects. Mutability decides the rest.
- Defaults: use `is None`, not `or`.
- Join once. Decode at the edge. Tokenizer, not len.
- Comprehensions are eager. Generators are lazy and single-use.

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_shared_lists_and_new_strings.py` | Shared lists and new strings | yes |
| `code/02_lab_see_shared_objects_with_your_eyes.py` | See shared objects with your eyes | yes |
| `code/03_a_safe_default_for_temperature.py` | A safe default for temperature | yes |
| `code/04_f_strings_slices_and_one_join.py` | f-strings, slices and one join | yes |
| `code/05_four_ways_to_build_collections.py` | Four ways to build collections | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/02_lab_see_shared_objects_with_your_eyes.py` prints:

```text
a is now [1, 2, 3]
abc ABC
(1, [2, 3])
TypeError: unhashable type: 'list'
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. An interviewer says Python is slow, so why does all of ML use it?**

- A. It is a bad fit, rewrite in C++
- B. Hot paths run in native code
- C. Python speed never matters

<details><summary>Answer</summary>

**B. Hot paths run in native code**. Hot paths are native. Tight pure-Python loops still hurt.

</details>

**2. What happens when you use the tuple (1, [2]) as a dict key?**

- A. TypeError, it is unhashable
- B. It works, tuples are immutable
- C. It works until the list changes

<details><summary>Answer</summary>

**A. TypeError, it is unhashable**. A tuple is only hashable if its contents are.

</details>

**3. With temperature = temperature or 0.7, what happens when the caller passes 0.0?**

- A. It stays 0.0
- B. It raises an error
- C. It becomes 0.7

<details><summary>Answer</summary>

**C. It becomes 0.7**. Zero and empty are valid values. Use `is None`.

</details>

**4. How do you know how many tokens you are sending to a model?**

- A. Use the model's tokenizer
- B. len of the text
- C. Count the words

<details><summary>Answer</summary>

**A. Use the model's tokenizer**. Budget tokens with the tokenizer, not len.

</details>

**5. You loop over the same generator expression twice. What does the second loop see?**

- A. The same items again
- B. It raises an error
- C. Nothing, it is empty

<details><summary>Answer</summary>

**C. Nothing, it is empty**. Generators run once. Need it twice? Use a list.

</details>

## Say it in the interview

**Python as glue, in three lines**

- Python is the glue. The expensive work runs in compiled code.
- New AI tooling lands in Python first.
- CPU work to libraries, asyncio for I/O, lockfile for dependencies.

**Mutability, in three lines**

- Names point at objects. Ask: is the object mutable?
- Shared state, hashing, concurrency.
- A tuple with a list inside is not hashable.

**Truthiness, in three lines**

- Falsy: empty, zero, None. Python checks __bool__, then __len__.
- `or` defaults erase valid zeros.
- Optional parameters: check `is None`.

**Strings, in three lines**

- Immutable strings: collect parts, join once.
- Decode at the edge, str inside, encode out.
- Measure tokens with the tokenizer.

**Comprehensions, in three lines**

- Need it all: comprehension. Use once: generator.
- sum(len(c) for c in chunks) builds no list.
- Complex logic belongs in a normal loop.

## Homework

- [ ] Explain Python as glue in under a minute.
- [ ] Hash (1, [2]) and read the error.
- [ ] Write a default that keeps 0.0.
- [ ] Loop over one generator twice.
