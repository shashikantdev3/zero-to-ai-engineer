# Python · Interview Quiz: Ten Questions Interviews Keep Asking

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Flatten a nested list, and the string trap
2. Flatten a nested dictionary to dot keys
3. Decorators and functools.wraps
4. The order of stacked decorators
5. Decorators with arguments
6. Mutable default arguments
7. Late binding in closures
8. Shallow versus deep copy
9. The GIL: threads, processes or asyncio
10. Retry with backoff and jitter
11. Rapid-fire round

## Key takeaways

- Trace line by line before answering
- Name the edge cases before you are asked
- Know what is shared and what is copied
- wraps always; built bottom up, run top down
- Cap, classify, jitter, and protect writes

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_flatten_a_nested_list.py` | Flatten a nested list | yes |
| `code/02_recurse_into_lists_only.py` | Recurse into lists only | yes |
| `code/03_flatten_a_nested_dictionary.py` | Flatten a nested dictionary | yes |
| `code/04_lab_flatten_unflatten_round_trip.py` | Flatten, unflatten, round trip | yes |
| `code/05_a_logging_decorator_from_scratch.py` | A logging decorator from scratch | yes |
| `code/06_two_decorators_on_one_function.py` | Two decorators on one function | yes |
| `code/07_a_decorator_that_takes_arguments.py` | A decorator that takes arguments | yes |
| `code/08_a_list_as_a_default_argument.py` | A list as a default argument | yes |
| `code/09_lambdas_created_in_a_loop.py` | Lambdas created in a loop | yes |
| `code/10_copying_a_nested_state.py` | Copying a nested state | yes |
| `code/11_capped_exponential_backoff.py` | Capped exponential backoff | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/04_lab_flatten_unflatten_round_trip.py` prints:

```text
{'a.b': 1, 'a.c': {}, 'd': 2}
{'a': {'b': 1, 'c': {}}, 'd': 2}
True
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. What does this code print?**

- A. A flat list ending in a, b
- B. A flat list ending in ab
- C. RecursionError

<details><summary>Answer</summary>

**C. RecursionError**. Test for list, not iterable. Strings recurse forever.

</details>

**2. What happens to the empty dict under c and the list under d?**

- A. Empty dict kept, list kept whole
- B. Empty dict dropped, list split by index
- C. Empty dict dropped, list kept whole

<details><summary>Answer</summary>

**A. Empty dict kept, list kept whole**. Empty dicts and lists are leaves unless you decide otherwise.

</details>

**3. What does the last line print?**

- A. wrapper None
- B. add None
- C. add Add two numbers.

<details><summary>Answer</summary>

**A. wrapper None**. Use functools.wraps, or every function is called wrapper.

</details>

**4. In what order do the labels print?**

- A. A, B, run, A, B
- B. B, A, run, A, B
- C. A, B, run, B, A

<details><summary>Answer</summary>

**C. A, B, run, B, A**. Built bottom up, run top down. A wraps B.

</details>

**5. What does print(hello.__name__) show?**

- A. wrapper
- B. deco
- C. hello

<details><summary>Answer</summary>

**B. deco**. Factory decorators need parentheses: @repeat(times=2).

</details>

**6. What does the second call, add_msg("b"), print?**

- A. A fresh list holding only b
- B. A list holding a and b
- C. A list holding only a

<details><summary>Answer</summary>

**B. A list holding a and b**. Default to None, create the list inside.

</details>

**7. What does the last line print?**

- A. NameError, i is gone
- B. [0, 1, 2]
- C. [2, 2, 2]

<details><summary>Answer</summary>

**C. [2, 2, 2]**. Closures read variables at call time. Bind with i=i.

</details>

**8. What does the last line print?**

- A. 2 1
- B. 1 1
- C. 2 2

<details><summary>Answer</summary>

**A. 2 1**. Shallow copies share inner objects. Snapshots need deepcopy.

</details>

**9. You must make 1,000 model API calls. Which approach do you choose?**

- A. asyncio, capped with a semaphore
- B. Multiprocessing, for true parallelism
- C. One thread per call

<details><summary>Answer</summary>

**A. asyncio, capped with a semaphore**. I/O-bound calls: asyncio, a semaphore, and a token bucket.

</details>

**10. A thousand clients share this schedule after an outage. What is missing?**

- A. More attempts before giving up
- B. Full jitter, a random delay
- C. A higher cap on the delay

<details><summary>Answer</summary>

**B. Full jitter, a random delay**. Classify, back off, cap, full jitter, idempotent writes.

</details>

## Homework

- [ ] Write both flattens from memory
- [ ] Predict a two-decorator stack, then run it
- [ ] Write the 1,000-calls answer in five sentences
