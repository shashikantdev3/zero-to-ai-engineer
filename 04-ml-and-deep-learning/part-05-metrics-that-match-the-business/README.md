# Machine Learning and Deep Learning · Part 5 of 28: Metrics That Match the Business

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Recall at budget (alert budget, precision at k)
2. Cost-weighted evaluation
3. Probability calibration
4. Metric uncertainty

## Key takeaways

- Capacity fixes k; measure recall within k
- Price mistakes; pick the lowest-cost threshold
- Ranking well is not being calibrated
- Bootstrap the paired difference; state positives

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_sample_data_and_running_totals.py` | Sample data and running totals | yes |
| `code/02_pool_the_counts_across_days.py` | Pool the counts across days | yes |
| `code/03_expected_cost_in_a_few_lines.py` | Expected cost in a few lines | yes |
| `code/04_lab_find_the_cheapest_threshold.py` | Find the cheapest threshold | yes |
| `code/05_data_sorted_by_time.py` | Data sorted by time | yes |
| `code/06_calibrate_then_check_the_curve.py` | Calibrate, then check the curve | yes |
| `code/07_validation_data_with_few_frauds.py` | Validation data with few frauds | yes |
| `code/08_paired_bootstrap_of_the_difference.py` | Paired bootstrap of the difference | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/04_lab_find_the_cheapest_threshold.py` prints:

```text
t=0.75 fp=1 cost=1030
t=0.5 fp=2 cost=1000
t=0.25 fp=3 cost=150
best: 0.25 cost: 150
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. Reviewers can check 200 flags a day. What should you report?**

- A. Recall within the top 200 flags
- B. Precision, because capacity is limited
- C. Accuracy across all transactions

<details><summary>Answer</summary>

**A. Recall within the top 200 flags**. Capacity fixes k, so ask recall within k

</details>

**2. Your cost model charges 50 per false flag. Where should 50 come from?**

- A. The business, with a sensitivity check
- B. The library's default setting
- C. Your own best engineering guess

<details><summary>Answer</summary>

**A. The business, with a sensitivity check**. Costs come from the business; show sensitivity

</details>

**3. Trained on 50/50 oversampled data, a case scores 0.5 in production. What does that mean?**

- A. Exactly a fifty percent fraud chance
- B. Much less than a fifty percent fraud chance
- C. More than a fifty percent fraud chance

<details><summary>Answer</summary>

**B. Much less than a fifty percent fraud chance**. Resampling breaks calibration; AUC only ranks

</details>

**4. PR-AUC went from 0.38 to 0.41. What do you ask before shipping?**

- A. Do the separate intervals overlap?
- B. Nothing, a gain is a gain
- C. How many frauds, and what interval?

<details><summary>Answer</summary>

**C. How many frauds, and what interval?**. Ask for positives and the paired interval

</details>

## Say it in the interview

**Recall at budget, in an interview**

- Capacity decides k; recall within k matters
- Weight recall by money lost
- Compare on PR-AUC, report recall at budget

**Cost-weighted, in an interview**

- Counts treat tiny and huge fraud alike
- Price each cell; minimise expected cost
- Cost per resolved task, not per token

**Calibration, in an interview**

- Ranking and calibration are different
- Recalibrate on later, held-out data
- Never trust confidence scores unchecked

**Uncertainty, in an interview**

- Never report a bare metric
- Zero in the interval means no win
- Always state the positive count

## Homework

- [ ] Change the false flag cost in the lab
- [ ] Write the recall at budget answer
- [ ] Explain why oversampling breaks calibration
- [ ] Bootstrap a smaller set; compare intervals
