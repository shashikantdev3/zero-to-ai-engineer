# Python · Part 25 of 25: How Python Frees Memory

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Reference counting and the cycle collector
2. weakref
3. __del__ and why to avoid it
4. Hunting a memory leak in a long-running service
5. Question drill: memory management

## Key takeaways

- Refcount frees now; gc handles cycles.
- Weak references don't keep objects alive.
- Clean up with context managers, not __del__.
- Suspects first, then compare snapshots.
- Don't blame the garbage collector first.

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_counting_references_in_code.py` | Counting references in code | yes |
| `code/02_a_cache_that_forgets.py` | A cache that forgets | yes |
| `code/03_lab_watch_objects_disappear.py` | Watch objects disappear | yes |
| `code/04_cleanup_with_weakref_finalize.py` | Cleanup with weakref.finalize | yes |
| `code/05_comparing_tracemalloc_snapshots.py` | Comparing tracemalloc snapshots | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/03_lab_watch_objects_disappear.py` prints:

```text
alive: True
after del: None
in cycle: True
after collect: None
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. When a function returns, why is its large local list freed straight away?**

- A. Its reference count reaches zero
- B. The garbage collector runs on every return
- C. It is not, memory is freed eventually

<details><summary>Answer</summary>

**A. Its reference count reaches zero**. Refcount zero means freed now, not eventually.

</details>

**2. What happens if you try to make a weak reference to a plain list?**

- A. It works like any other object
- B. It raises a TypeError
- C. It quietly returns None

<details><summary>Answer</summary>

**B. It raises a TypeError**. Lists can't be weakly referenced; wrap them.

</details>

**3. You close a database connection inside __del__. What could go wrong?**

- A. Python forbids defining dunder del
- B. The connection closes twice
- C. Cleanup may happen late or never

<details><summary>Answer</summary>

**C. Cleanup may happen late or never**. Use a context manager, not __del__.

</details>

**4. Resident memory stayed at eight gigabytes after a batch. Do you have a leak?**

- A. Only if it grows on the next batch
- B. Yes, the garbage collector is broken
- C. Yes, memory should drop right away

<details><summary>Answer</summary>

**A. Only if it grows on the next batch**. A leak keeps growing under steady load.

</details>

**5. A service's memory keeps growing. Where do you look first?**

- A. Moving cleanup into dunder del
- B. Unbounded caches and growing collections
- C. Tuning the garbage collector thresholds

<details><summary>Answer</summary>

**B. Unbounded caches and growing collections**. Look for things that only grow first.

</details>

## Say it in the interview

**Say it in the interview**

- Freed the moment the last reference goes.
- The collector exists only for cycles.
- Real leaks: unbounded caches, growing lists.

**Say it in the interview**

- Refer to it without keeping it alive.
- Fixes the lru_cache-on-a-method leak.
- Wrap ints, lists and dicts first.

**Say it in the interview**

- It may not run, and errors vanish.
- Unpredictable in cycles; can resurrect.
- Context managers, or weakref.finalize.

**Say it in the interview**

- Start with things that only grow.
- Two tracemalloc snapshots, compared by line.
- Watch for growth under steady load.

## Homework

- [ ] Print gc.get_threshold() on your Python
- [ ] Build a WeakValueDictionary cache
- [ ] Swap one __del__ for a context manager
- [ ] Compare two tracemalloc snapshots
