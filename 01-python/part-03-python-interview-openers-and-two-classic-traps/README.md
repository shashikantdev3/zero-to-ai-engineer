# Python · Part 3 of 25: Python Interview Openers and Two Classic Traps

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Answering "how strong is your Python?"
2. Python version currency, 3.9 to 3.14
3. Question drill: core language
4. Answering a Python concept question in four beats
5. Mutable default arguments
6. Late binding in closures

## Key takeaways

- Give a specific map, not a score.
- Know version features; check the minimum runtime.
- Object reference, O(1) sets, sort returns None.
- Definition, mechanism, bite, trade-off. Then stop.
- Defaults built once; use a None sentinel.
- Closures look up at call time; bind the value.

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_fail_fast_on_an_old_runtime.py` | Fail fast on an old runtime | yes |
| `code/02_beat_four_in_code_the_fix.py` | Beat four in code: the fix | yes |
| `code/03_the_none_sentinel_fix.py` | The None sentinel fix | yes |
| `code/04_lab_watch_a_default_leak.py` | Watch a default leak | yes |
| `code/05_the_bug_and_two_fixes.py` | The bug and two fixes | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/04_lab_watch_a_default_leak.py` prints:

```text
bad a: ['a']
bad b: ['a', 'b']
defaults: (['a', 'b'],)
good a: ['a']
good b: ['b']
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. An interviewer asks how strong your Python is. What is the best kind of answer?**

- A. Expert in everything I use
- B. A specific map of strong and lighter areas
- C. Nine out of ten

<details><summary>Answer</summary>

**B. A specific map of strong and lighter areas**. A number invites the hardest probe; a map lets you steer

</details>

**2. Does the JIT make Python 3.13 much faster by default?**

- A. Yes, it is on by default
- B. Yes, but only on Linux
- C. No, it is experimental and off

<details><summary>Answer</summary>

**C. No, it is experimental and off**. The 3.13 JIT is experimental and off by default

</details>

**3. If you write x equals items dot sort, what is x?**

- A. None
- B. A sorted copy of items
- C. The sorted list

<details><summary>Answer</summary>

**A. None**. list.sort returns None; sorted returns a new list

</details>

**4. What is the most common way to fail a Python concept question?**

- A. Giving only the definition
- B. Mentioning the Python version
- C. Giving a concrete bug example

<details><summary>Answer</summary>

**A. Giving only the definition**. Definition alone sounds like recall; stop before sixty seconds

</details>

**5. Does Python reset a default argument on each call?**

- A. Yes, every call gets a fresh one
- B. No, it is built once and shared
- C. Only for lists and dicts

<details><summary>Answer</summary>

**B. No, it is built once and shared**. Defaults are built once; __defaults__ holds the shared object

</details>

**6. Would using def instead of lambda inside the loop fix late binding?**

- A. Yes, but only inside a list
- B. Yes, lambdas are the buggy part
- C. No, every closure binds the same way

<details><summary>Answer</summary>

**C. No, every closure binds the same way**. It is the binding rule, not lambda

</details>

## Say it in the interview

**Say it: your Python strength**

- Specific beats a number.
- Metaprogramming: understood, not shipped.
- Push on any of those; I will show you.

**Say it: version currency**

- 3.11: TaskGroup, ExceptionGroup, timeout, speed-up.
- 3.14 free-threading: supported, still optional.
- Check the minimum runtime first.

**Say it: four beats in action**

- Defaults are evaluated once, at def time.
- One request's history leaks into the next.
- Fix: None default; dataclasses use default_factory.

**Say it: mutable defaults**

- Evaluated once, shared across calls.
- Looks like a leak, or crossed conversations.
- None sentinel, or default_factory.

**Say it: late binding**

- Closures capture variables, looked up at call time.
- Every tool handler calls the last tool.
- Default argument, partial, or factory function.

## Homework

- [ ] Write your fluent and lighter Python areas
- [ ] Add a sys.version_info check to a script
- [ ] Answer late binding in four beats, timed
- [ ] Fix a list default with a None sentinel
