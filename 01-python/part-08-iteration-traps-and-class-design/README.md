# Python · Part 8 of 25: Iteration Traps and Class Design

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. PEP 479: StopIteration inside a generator becomes RuntimeError
2. Generator expressions: the outermost iterable is evaluated eagerly
3. itertools.product and combinations for evaluation sweeps
4. Question drill: iteration
5. Classes, method types, __init__ versus __new__, and dunder methods
6. Composition, inheritance, abstract base classes and Protocol

## Key takeaways

- Escaping StopIteration is a RuntimeError since 3.7
- Outermost iterable eager, the rest lazy
- product for grids, combinations for pairs
- send resumes; return value reaches yield from
- __new__ builds; pair __eq__ with __hash__
- Composition first; ABC nominal, Protocol structural

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_bare_next_versus_islice.py` | Bare next versus islice | yes |
| `code/02_mutate_versus_rebind.py` | Mutate versus rebind | yes |
| `code/03_lab_watch_the_eager_and_lazy_parts.py` | Watch the eager and lazy parts | yes |
| `code/04_an_evaluation_sweep_grid.py` | An evaluation sweep grid | yes |
| `code/05_subclassing_str_with_new.py` | Subclassing str with __new__ | yes |
| `code/06_chunk_init_repr_len.py` | Chunk: init, repr, len | yes |
| `code/07_chunk_eq_and_hash_together.py` | Chunk: eq and hash together | yes |
| `code/08_protocol_and_abc_side_by_side.py` | Protocol and ABC side by side | yes |
| `code/09_the_agent_holds_its_parts.py` | The agent holds its parts | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/03_lab_watch_the_eager_and_lazy_parts.py` prints:

```text
mutated: [1, 2, 3, 4]
rebound: [1, 2, 3]
None fails at creation
filter runs lazily: 5
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. On Python 3.7 or later, a bare next call inside a generator runs out. What happens?**

- A. A RuntimeError is raised
- B. The loop quietly ends
- C. The generator yields None

<details><summary>Answer</summary>

**A. A RuntimeError is raised**. Escaping StopIteration becomes RuntimeError.

</details>

**2. You write a generator expression that loops over None. When does the error appear?**

- A. Never, it just yields nothing
- B. Immediately, when it is created
- C. Only when you consume it

<details><summary>Answer</summary>

**B. Immediately, when it is created**. The outermost iterable is evaluated at creation.

</details>

**3. Does combinations of a, b, c and d, two at a time, include both a b and b a?**

- A. Yes, both orders appear
- B. Only when the input is sorted
- C. No, each pair appears once

<details><summary>Answer</summary>

**C. No, each pair appears once**. Ordered pairs need permutations.

</details>

**4. A generator ends with return forty two. What does a plain for loop over it receive?**

- A. Forty two as the last item
- B. A RuntimeError at the end
- C. Nothing, it never sees the value

<details><summary>Answer</summary>

**C. Nothing, it never sees the value**. Return values reach yield from, not for loops.

</details>

**5. You subclass int so the stored value differs from what was passed. Which method does the work?**

- A. Dunder repr
- B. Dunder new
- C. Dunder init

<details><summary>Answer</summary>

**B. Dunder new**. __new__ builds; __init__ only initialises.

</details>

**6. With a runtime checkable Protocol, what does is instance actually check?**

- A. Only that the method names exist
- B. The full method signatures and types
- C. That the class inherits the Protocol

<details><summary>Answer</summary>

**A. Only that the method names exist**. runtime_checkable tests names, not signatures.

</details>

## Say it in the interview

**The**

- It used to truncate output silently.
- Since 3.7, it becomes a RuntimeError.
- Use islice, or next with a default.

**The**

- Outermost iterable now, the rest lazily.
- Mutation seen, rebinding not seen.
- Filter errors surface far from creation.

**The**

- product for the sweep, lazily.
- Count the grid before you run it.
- combinations for pairwise judging.

**The**

- __new__ allocates, __init__ fills in.
- __new__ for immutables and caching.
- Define __eq__? Define __hash__ too.

**The**

- Composition first: swappable, mockable parts.
- ABC: nominal, fails when incomplete.
- Protocol: structural, fits third-party clients.

## Homework

- [ ] Trigger the PEP 479 RuntimeError
- [ ] Size a product grid before looping
- [ ] Define only __eq__, then hash it
- [ ] Satisfy a Protocol without inheriting
