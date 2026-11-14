# Evaluation · Part 1 of 11: Evaluation Foundations: Measure, Don't Guess

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Evals, not vibes
2. Golden set
3. Past failures as regression cases
4. Error analysis and failure taxonomy

## Key takeaways

- Fixed cases plus a number beat vibes
- Real, redacted, versioned, tagged cases
- Every failure becomes a permanent case
- Count failure types, fix the biggest first

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_two_golden_cases_in_python.py` | Two golden cases in Python | yes |
| `code/02_redact_the_query_first.py` | Redact the query first | yes |
| `code/03_save_the_regression_case.py` | Save the regression case | yes |
| `code/04_lab_lab_redact_before_you_save.py` | Lab: redact before you save | yes |
| `code/05_counting_failure_labels.py` | Counting failure labels | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/04_lab_lab_redact_before_you_save.py` prints:

```text
Mail [EMAIL] re leave
Call [PHONE] now
Bonus for 2023?
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. Your team says the business tried it and was happy. What is missing?**

- A. A bigger, newer model
- B. A fixed set of cases and a score
- C. More people trying it for longer

<details><summary>Answer</summary>

**B. A fixed set of cases and a score**. Without a fixed set and a number, you cannot compare

</details>

**2. The app works in testing but fails for real users. Why?**

- A. Test questions were tidy, real ones were not
- B. The model forgets things over time
- C. The test set was too large

<details><summary>Answer</summary>

**A. Test questions were tidy, real ones were not**. Build the set from real questions, not invented ones

</details>

**3. You fixed the prompt. How do you know it stays fixed after a model upgrade?**

- A. Note the fix in the changelog
- B. Test it by hand once more
- C. Add the case to the golden set

<details><summary>Answer</summary>

**C. Add the case to the golden set**. A bug is not fixed until it is a test

</details>

**4. Before choosing eval metrics, what should you do first?**

- A. Read and label real failures
- B. Pick metrics from a library list
- C. Average every available metric

<details><summary>Answer</summary>

**A. Read and label real failures**. Generic metrics before error analysis often measure the wrong thing

</details>

## Say it in the interview

**Say it in the interview**

- Test it like a service, with repeated runs
- Golden set, scored by code, judge and humans
- Gate every change, then watch production

**Say it in the interview**

- My contract for what good looks like
- Redacted, access controlled, with refusal cases
- Past failures are the most valuable cases

**Say it in the interview**

- A bug is not fixed until it is a test
- Replay, root cause, fix, redact, add
- Grow evals from real pain

**Say it in the interview**

- Read failures before adding any metric
- The top categories decide the work
- Quote the MAST grouping, not a percentage

## Homework

- [ ] Write down what good means
- [ ] Collect ten real questions with outcomes
- [ ] Add one case that must be refused
- [ ] Label five failures and count them
