# Python · Part 12 of 25: Finally, Error Chains, Groups and Generics

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. return inside finally, from None, __cause__ and __context__
2. EAFP versus LBYL, and catching at the boundary
3. Question drill: context managers and errors
4. ExceptionGroup and except*
5. PEP 695 type parameter syntax and the type statement

## Key takeaways

- finally's return wins; from sets cause.
- Try and handle; catch once at the edge.
- Enter fails, exit never runs.
- except* handles each type in a group.
- Brackets for generics; hints still not enforced.

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_finally_overrides_the_return.py` | finally overrides the return | yes |
| `code/02_translate_errors_with_from_none.py` | Translate errors with from None | yes |
| `code/03_lab_watch_cause_and_context_get_set.py` | Watch cause and context get set | yes |
| `code/04_check_first_versus_just_try.py` | Check first versus just try | yes |
| `code/05_build_the_exception_group.py` | Build the exception group | yes |
| `code/06_handle_each_type_once.py` | Handle each type once | yes |
| `code/07_a_generic_function_and_class.py` | A generic function and class | yes |
| `code/08_a_bound_and_a_recursive_alias.py` | A bound and a recursive alias | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/03_lab_watch_cause_and_context_get_set.py` prints:

```text
cause: KeyError('k')
ctx: KeyError('k')
cause: None
ctx: KeyError('k')
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. A try block raises a value error, and finally returns a string. What does the call give you?**

- A. The value error, raised to the caller
- B. The string from finally
- C. A syntax error when defined

<details><summary>Answer</summary>

**B. The string from finally**. A return in finally swallows the exception.

</details>

**2. Your code checks that a file exists, and another process deletes it before you open it. What happens?**

- A. Open raises file not found anyway
- B. The check prevents any error
- C. Python retries the check for you

<details><summary>Answer</summary>

**A. Open raises file not found anyway**. The race still raises, so you need except.

</details>

**3. If __enter__ raises an exception, does __exit__ run?**

- A. No, so enter must clean up itself
- B. Yes, exit always runs
- C. Only when exit returns True

<details><summary>Answer</summary>

**A. No, so enter must clean up itself**. If enter raises, exit never runs.

</details>

**4. You wrap a task group in a plain except timeout error, and one task times out. Does your handler run?**

- A. Only if every task times out
- B. Yes, except matches the timeout directly
- C. No, the timeout arrives inside a group

<details><summary>Answer</summary>

**C. No, the timeout arrives inside a group**. Plain except misses errors wrapped in a group.

</details>

**5. After you switch to the new generic syntax, does Python check argument types at runtime?**

- A. Yes, the brackets turn on checking
- B. No, hints are still not enforced
- C. Only inside generic classes

<details><summary>Answer</summary>

**B. No, hints are still not enforced**. New syntax, same runtime: hints not enforced.

</details>

## Say it in the interview

**Say it in the interview**

- A return in finally swallows exceptions.
- from sets cause; plain raise sets context.
- from None only for implementation details.

**Say it in the interview**

- Try it, handle the specific failure.
- Checking first races and doubles work.
- Fail loudly inside, catch once at the edge.

**Say it in the interview**

- ExceptionGroup bundles; except* splits by type.
- Unplanned errors still propagate.
- Plain except misses timeouts inside groups.

**Say it in the interview**

- Old TypeVar style is noisy and leaks.
- Brackets on the definition; type for recursion.
- Needs 3.12; earlier it is a syntax error.

## Homework

- [ ] Run the finally example, watch the error vanish
- [ ] Rewrite one LBYL check as EAFP
- [ ] Catch a two-error group with except*
- [ ] Convert one TypeVar function to brackets
