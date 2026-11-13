# Python · Part 11 of 25: Cleanup, Errors, Type Hints and Pydantic

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Context managers
2. Exceptions: hierarchy, custom exceptions, raise from, else and finally
3. Type hints: Optional, Union, Literal, TypedDict, Protocol and generics
4. Pydantic v2
5. An exception inside __enter__, and the transaction manager

## Key takeaways

- Cleanup is guaranteed. Wrap yield in try, finally
- Typed errors, raise from, else, finally
- Hints are checked by tools, not runtime
- Pydantic checks shape. You check truth
- Failed __enter__ means no __exit__

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_a_timing_span_with_contextmanager.py` | A Timing Span With contextmanager | yes |
| `code/02_suppress_and_exitstack.py` | suppress and ExitStack | yes |
| `code/03_lab_safe_versus_leaky_cleanup.py` | Safe Versus Leaky Cleanup | yes |
| `code/04_a_small_error_hierarchy.py` | A Small Error Hierarchy | yes |
| `code/05_raise_from_else_and_finally.py` | raise from, else and finally | yes |
| `code/06_literal_typeddict_and_generics.py` | Literal, TypedDict and Generics | yes |
| `code/07_declaring_the_ticket_model.py` | Declaring the Ticket Model | yes |
| `code/08_a_custom_field_rule.py` | A Custom Field Rule | yes |
| `code/09_validate_dump_or_collect_errors.py` | Validate, Dump, or Collect Errors | yes |
| `code/10_enter_cleans_up_its_own_mess.py` | Enter Cleans Up Its Own Mess | yes |
| `code/11_commit_roll_back_always_release.py` | Commit, Roll Back, Always Release | yes |
| `code/12_a_rollback_that_cannot_mask.py` | A Rollback That Cannot Mask | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/03_lab_safe_versus_leaky_cleanup.py` prints:

```text
safe: cleanup ran
safe: error escaped
leaky: error escaped
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. In a generator-based context manager without try and finally, what happens to the cleanup when the body raises?**

- A. The code after yield never runs
- B. Python silently ignores the error
- C. Cleanup runs, then the error spreads

<details><summary>Answer</summary>

**A. The code after yield never runs**. No finally around yield means no cleanup on error

</details>

**2. A model call is wrapped in except Exception followed by pass. What is the real problem?**

- A. It also catches control C
- B. It makes the model call slower
- C. You cannot tell if or why it failed

<details><summary>Answer</summary>

**C. You cannot tell if or why it failed**. Log, classify, then re-raise or return a typed error

</details>

**3. The pick function expects small or large. What happens at runtime if you call it with medium?**

- A. It raises a type error
- B. It returns medium without complaint
- C. It raises a value error

<details><summary>Answer</summary>

**B. It returns medium without complaint**. Tools check hints. Python does not

</details>

**4. The model's JSON passes your Pydantic model. Is the data now correct?**

- A. Yes, validation proves it is correct
- B. Only its shape is checked, not truth
- C. Only if strict mode is on

<details><summary>Answer</summary>

**B. Only its shape is checked, not truth**. Validation checks shape, not truth

</details>

**5. Does a with statement guarantee cleanup even when dunder enter raises after acquiring a connection?**

- A. No, dunder exit is skipped entirely
- B. Yes, dunder exit always runs
- C. Only if dunder exit returns False

<details><summary>Answer</summary>

**A. No, dunder exit is skipped entirely**. __exit__ runs only if __enter__ finished

</details>

## Say it in the interview

**Context Managers in an Interview**

- with exists to guarantee cleanup
- Returning True swallows errors. Almost never do it
- ExitStack for many resources, async with for clients

**Exceptions in an Interview**

- Custom hierarchy: decide by type
- raise from keeps the cause. No bare except
- 3.11: ExceptionGroup, except*, add_note

**Type Hints in an Interview**

- Hints: documentation a checker can verify
- Literal, TypedDict, Protocol, generics: each has a job
- Untrusted boundary? Add Pydantic

**Pydantic in an Interview**

- Pydantic is the gate at untrusted boundaries
- v2: model_validate and model_dump
- Shape is not truth. Check meaning after

**Transactions in an Interview**

- Enter fails? Enter cleans up itself
- Commit or roll back. Always release
- Return False. Never swallow database errors

## Homework

- [ ] Write a timing span with try and finally
- [ ] Build a small custom exception hierarchy
- [ ] Catch a Literal mismatch with mypy
- [ ] Validate bad JSON and read e.errors()
