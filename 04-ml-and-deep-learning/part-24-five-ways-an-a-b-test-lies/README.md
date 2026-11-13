# Machine Learning and Deep Learning · Part 24 of 28: Five Ways an A/B Test Lies

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Sample ratio mismatch
2. Simpson's paradox
3. Novelty, primacy and multiple comparisons
4. Interference and switchback designs
5. Interleaving

## Key takeaways

- SRM: chi-square first, strict threshold, per segment
- Simpson: check allocation, trust within-segment results
- Wait out time effects; one primary metric
- Interference: cluster split or switchback
- Interleaving compares rankers, not a deployment

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_an_srm_check_with_scipy.py` | An SRM Check With SciPy | yes |
| `code/02_lab_same_ratio_different_verdict.py` | Same Ratio, Different Verdict | yes |
| `code/03_allocation_share_per_day.py` | Allocation Share per Day | yes |
| `code/04_correcting_many_p_values.py` | Correcting Many p-values | yes |
| `code/05_team_draft_taking_a_pick.py` | Team Draft: Taking a Pick | yes |
| `code/06_team_draft_building_the_list.py` | Team Draft: Building the List | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/02_lab_same_ratio_different_verdict.py` prints:

```text
1000 p=0.2059 ok
100000 p=0.0000 SRM
800000 p=0.0003 SRM
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. A test shows a 48/52 split. Is that a sample ratio mismatch?**

- A. No, splits are never exact
- B. It depends on how many users
- C. Yes, any gap over one point

<details><summary>Answer</summary>

**B. It depends on how many users**. Sample size decides whether a split is suspicious

</details>

**2. A ramped test wins every day but loses on the pooled total. What do you trust?**

- A. Whichever number has the smaller p-value
- B. The pooled total, it has more data
- C. Within-day results, after checking allocation

<details><summary>Answer</summary>

**C. Within-day results, after checking allocation**. Ramped test: ask if allocation stayed constant

</details>

**3. You tracked 20 metrics. One secondary metric is significant at 5%. Ship it?**

- A. Yes, if two more days agree
- B. No, one false win is expected
- C. Yes, significant means it is real

<details><summary>Answer</summary>

**B. No, one false win is expected**. Never ship on a lucky secondary metric

</details>

**4. Why is user-level randomisation risky in a ride-sharing app?**

- A. Control riders share drivers with treated ones
- B. Drivers refuse to join experiments
- C. There are too few riders to split

<details><summary>Answer</summary>

**A. Control riders share drivers with treated ones**. Two-sided marketplace: randomise above the user

</details>

**5. What does interleaving tell you about latency or errors?**

- A. Nothing, it only compares ranking preference
- B. Whether the release is safe to ship
- C. Which ranker responds faster

<details><summary>Answer</summary>

**A. Nothing, it only compares ranking preference**. Interleaving measures preference, not release safety

</details>

## Say it in the interview

**Say It: Sample Ratio Mismatch**

- The split I got is not the split I set
- Chi-square, strict threshold, sample size decides
- Mismatch found: stop and find the cause

**Say It: Simpson's Paradox**

- Different segment mix, often from a ramp
- Unbalanced? Trust within-segment results

**Say It: Novelty and Many Metrics**

- Plot by exposure day; do not decide early
- One primary metric, corrected if many matter

**Say It: Interference**

- Marketplaces break the independence assumption
- City split, switchback, or DiD

**Say It: Interleaving**

- One list, clicks credited to the supplier
- Paired, so far more sensitive
- Not deployment: still roll out the winner

## Homework

- [ ] Rerun the lab with a 49/51 split
- [ ] Name one product with interference, plus fix
- [ ] Write team draft from memory
- [ ] Explain Simpson's paradox in two sentences
