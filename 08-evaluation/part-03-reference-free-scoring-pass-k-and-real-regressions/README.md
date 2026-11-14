# Evaluation · Part 3 of 11: Reference-free scoring, pass^k and real regressions

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Reference-based and reference-free evaluation
2. Run several times: pass@k and pass^k
3. Fixed sample, sample size and confidence intervals
4. Case-by-case regression diff

## Key takeaways

- Reference: correctness. Reference-free: properties only.
- Run several times; choose pass@k or pass^k
- Fixed sample, intervals, paired test
- Diff case by case; critical failures block

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_two_judges_one_answer.py` | Two judges, one answer | yes |
| `code/02_running_one_case_k_times.py` | Running one case k times | yes |
| `code/03_the_unbiased_pass_k_estimator.py` | The unbiased pass@k estimator | yes |
| `code/04_a_wilson_interval_in_code.py` | A Wilson interval in code | yes |
| `code/05_mcnemar_on_paired_results.py` | McNemar on paired results | yes |
| `code/06_the_regression_diff_in_code.py` | The regression diff in code | yes |
| `code/07_lab_average_up_release_down.py` | Average up, release down | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/07_lab_average_up_release_down.py` prints:

```text
old average: 0.5
new average: 0.75
broke: ['q1']
fixed: ['q2', 'q3']
ship? NO
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. Groundedness is 98%. What does that tell you?**

- A. Answers are correct
- B. The index is up to date
- C. Answers match the retrieved context

<details><summary>Answer</summary>

**C. Answers match the retrieved context**. Groundedness is faithfulness, not correctness

</details>

**2. Temperature is zero. Is one run per case enough?**

- A. No, outputs can still vary
- B. Yes, if the prompt is short
- C. Yes, zero means deterministic

<details><summary>Answer</summary>

**A. No, outputs can still vary**. Temperature zero does not guarantee determinism

</details>

**3. B scores 92%, A scored 90%, on the same 50 cases. Ship B?**

- A. Not yet: count flips, run paired test
- B. Yes, two points up is a win
- C. Just compare the two separate intervals

<details><summary>Answer</summary>

**A. Not yet: count flips, run paired test**. Small rise, small set: show the paired test

</details>

**4. The average is up 3 points on the same cases. Safe to ship?**

- A. Yes, the average went up
- B. Only after a case-by-case diff
- C. Yes, three points is a lot

<details><summary>Answer</summary>

**B. Only after a case-by-case diff**. The average hides what broke

</details>

## Say it in the interview

**Say it in the interview**

- Golden set: reference-based, measures correctness
- Live traffic: reference-free, like groundedness
- Pair it with freshness monitoring

**Say it in the interview**

- One run per case hides variance
- Per-case pass rate, plus the worst run
- Agents: pass^k. Picked drafts: pass@k.

**Say it in the interview**

- Same fixed sample, or you compare datasets
- Fifty cases at 90%: about 79 to 96
- Paired test, plus hard gates for critical cases

**Say it in the interview**

- Average up does not mean nothing broke
- Critical regression blocks release
- I know from the diff

## Homework

- [ ] Run five cases five times each
- [ ] Compute pass@1 and pass@3 with the estimator
- [ ] Compute a Wilson interval for your score
- [ ] Diff two versions; list broke and fixed
