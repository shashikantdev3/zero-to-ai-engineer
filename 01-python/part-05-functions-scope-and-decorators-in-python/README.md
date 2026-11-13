# Python · Part 5 of 25: Functions, Scope and Decorators in Python

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Function arguments, *args, **kwargs and forwarding
2. Scope: LEGB, global and nonlocal
3. Closures, first-class functions, partial and reduce
4. Decorators from scratch and functools.wraps
5. Decorators with arguments, class-based decorators and stacking order

## Key takeaways

- / and * control how arguments are passed
- LEGB, decided at compile time
- Closures hold references, not copies
- f = dec(f), and always use wraps
- Factories need (), top decorator is outermost

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_call_model_and_a_wrapper.py` | call_model and a wrapper | yes |
| `code/02_a_counter_with_nonlocal.py` | A counter with nonlocal | yes |
| `code/03_scoring_tools_and_folding.py` | Scoring, tools and folding | yes |
| `code/04_a_timing_decorator.py` | A timing decorator | yes |
| `code/05_the_async_version.py` | The async version | yes |
| `code/06_a_retry_factory.py` | A retry factory | yes |
| `code/07_a_class_based_decorator_stacked.py` | A class-based decorator, stacked | yes |
| `code/08_lab_watch_the_stacking_order.py` | Watch the stacking order | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/08_lab_watch_the_stacking_order.py` prints:

```text
enter outer
enter inner
hi dev greet
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. A function accepts double star kwargs, and you misspell temperature when calling it. What happens?**

- A. Python raises a type error
- B. The typo is silently swallowed
- C. Python fixes the spelling

<details><summary>Answer</summary>

**B. The typo is silently swallowed**. kwargs hides typos unless you validate keys

</details>

**2. A function reads a name, then assigns it later. Why does Python raise unbound local error?**

- A. Scope is decided at compile time
- B. Assignment deletes the global
- C. The global was not set yet

<details><summary>Answer</summary>

**A. Scope is decided at compile time**. Scope is fixed at compile time

</details>

**3. When a closure captures a variable, does it copy the value?**

- A. Only for numbers and strings
- B. Yes, it copies the value
- C. No, it references the variable cell

<details><summary>Answer</summary>

**C. No, it references the variable cell**. Closures capture variables, not values

</details>

**4. Your tool schema shows star args and double star kwargs instead of real parameters. What did you forget?**

- A. A return statement
- B. functools wraps on the wrapper
- C. An async wrapper

<details><summary>Answer</summary>

**B. functools wraps on the wrapper**. wraps is not cosmetic: it sets __wrapped__

</details>

**5. Retry is a decorator factory, but you write at sign retry with no parentheses. What happens?**

- A. The function is passed as times
- B. Retry uses its default of three
- C. Python raises a syntax error

<details><summary>Answer</summary>

**A. The function is passed as times**. A factory needs parentheses: @retry()

</details>

## Say it in the interview

**Say it in the interview**

- Make risky parameters keyword-only
- Forwarding lets a decorator wrap anything
- Avoid kwargs in public APIs: typos vanish

**Say it in the interview**

- Local, enclosing, global, built-in
- nonlocal: counters without a class
- Module-level mutable state is a concurrency risk

**Say it in the interview**

- Functions as values: registries and harnesses
- partial beats a lambda for pre-binding
- Prefer sum or a loop over reduce

**Say it in the interview**

- Decorators handle cross-cutting concerns
- Always use functools.wraps
- Async target, async wrapper

**Say it in the interview**

- Config, decorator, wrapper
- Class decorators hold state like counters
- Stacking order is a deliberate choice

## Homework

- [ ] Write a function using / and *
- [ ] Build a nonlocal counter, then break it
- [ ] Write a timed decorator with functools.wraps
- [ ] Stack retry and timing both ways
