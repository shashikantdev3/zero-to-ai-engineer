# Python · Part 19 of 25: Leaked Keys, Test Doubles, Logs and Imports

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Secrets in Git history
2. Mock, stub and fake; assert the call, not the reply
3. Logging discipline: named loggers, lazy formatting, log.exception and levels
4. Modules, sys.modules and circular imports

## Key takeaways

- Leaked key: rotate first, rewrite is cleanup.
- Assert the call, not the reply.
- Named, lazy, log.exception, meaningful levels.
- Cached once. Fix cycles with a third module.

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_cleaning_history_after_rotation.py` | Cleaning history after rotation | yes |
| `code/02_re_add_origin_then_force_push.py` | Re-add origin, then force push | yes |
| `code/03_the_code_under_test.py` | The code under test | yes |
| `code/04_asserting_the_call.py` | Asserting the call | yes |
| `code/05_a_filter_stamps_the_correlation_id.py` | A filter stamps the correlation id | yes |
| `code/06_lazy_formatting_and_log_exception.py` | Lazy formatting and log.exception | yes |
| `code/07_lab_prove_lazy_formatting_yourself.py` | Prove lazy formatting yourself | yes |
| `code/08_type_only_imports.py` | Type-only imports | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/07_lab_prove_lazy_formatting_yourself.py` prints:

```text
percent-s formatted: 0
f-string formatted: 1
logger name: app.retriever
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. A key was deleted in the next commit, and the repo is private. What comes first?**

- A. Force push a rewritten history
- B. Nothing, the repo is private
- C. Revoke and rotate the key

<details><summary>Answer</summary>

**C. Revoke and rotate the key**. Rotate first. Private and force pushed are not safe.

</details>

**2. One key sits inside config dot py. Which approach removes only the key from history?**

- A. Replace text with an expressions file
- B. Remove config dot py with invert paths
- C. Delete the line in a new commit

<details><summary>Answer</summary>

**A. Replace text with an expressions file**. Invert paths deletes the file. Replace text edits it.

</details>

**3. Your unit test asserts that the model's answer contains the right fact. What goes wrong?**

- A. It fails randomly when the model rephrases
- B. Nothing, it is the strongest test
- C. It only slows down CI

<details><summary>Answer</summary>

**A. It fails randomly when the model rephrases**. Assert the call. Evaluate quality separately.

</details>

**4. Inside an except block, someone calls log dot error with an f-string of the exception. What is missing?**

- A. The logger name
- B. The traceback
- C. The log level

<details><summary>Answer</summary>

**B. The traceback**. Inside except, use log.exception.

</details>

**5. A teammate fixes a circular import by importing inside a function. Is the design fixed?**

- A. Yes, if the tests pass
- B. No, fix the dependency direction
- C. Yes, the cycle is gone

<details><summary>Answer</summary>

**B. No, fix the dependency direction**. Workarounds hide cycles. Fix the direction.

</details>

## Say it in the interview

**Answering the leaked key question**

- Rotate the key first, then check usage logs.
- History rewrite is cleanup, not the fix.
- Scan, block the push, use a vault.

**Answering the test doubles question**

- Stub answers. Mock records. Fake works.
- Assert the call, not the reply.
- Happy path, boundary, failure.

**Answering the logging question**

- Named loggers. Configure once.
- Lazy arguments. log.exception in except.
- Correlation ids. No prompts in logs.

**Answering the imports question**

- First import runs it. Then it is cached.
- Cycles: extract the shared piece.
- Tactical: local, module, TYPE_CHECKING.

## Homework

- [ ] Ignore .env and enable secret scanning
- [ ] Write a Mock test on call_args.kwargs
- [ ] Swap an f-string log for %s arguments
- [ ] Sketch your imports and find a cycle
