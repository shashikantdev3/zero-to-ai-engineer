# Machine Learning and Deep Learning · Part 22 of 28: Drift, Monitoring, Retraining and Fallback

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Population stability index, properly
2. Diagnosing a silently degrading model
3. Four monitoring layers
4. Retraining triggers and evaluation-set versioning
5. Model fallback

## Key takeaways

- PSI ranks drift; baseline your own alerts
- Metric, pipeline, drift, then retrain
- Watch the data and model layers
- Triggers, backstop, versioned eval set
- Cache, rules, or human; never no plan

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_a_psi_function.py` | A PSI function | yes |
| `code/02_an_alert_level_from_resampling.py` | An alert level from resampling | yes |
| `code/03_lab_watch_psi_shrink_with_more_rows.py` | Watch PSI shrink with more rows | yes |
| `code/04_accuracy_by_week_and_segment.py` | Accuracy by week and segment | yes |
| `code/05_an_alert_config_as_data.py` | An alert config, as data | yes |
| `code/06_a_stand_in_model_that_times_out.py` | A stand-in model that times out | yes |
| `code/07_falling_back_on_timeout.py` | Falling back on timeout | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/03_lab_watch_psi_shrink_with_more_rows.py` prints:

```text
n=100: PSI 0.337
n=1000: PSI 0.028
n=10000: PSI 0.005
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. A feature's PSI is 0.3. What do you ask before retraining?**

- A. Rows, bins, and does the model use it?
- B. Which model version should we retrain?
- C. Is this a Jensen-Shannon score?

<details><summary>Answer</summary>

**A. Rows, bins, and does the model use it?**. Context first: rows, bins, feature importance

</details>

**2. Accuracy dropped. Why is retraining first a risky move?**

- A. Retraining never fixes drift
- B. Recent data is always too small
- C. A broken feature gets baked in

<details><summary>Answer</summary>

**C. A broken feature gets baked in**. Find the cause before you retrain

</details>

**3. Dashboards are green. Which layer shows a feature silently arriving null?**

- A. The business metric dashboard
- B. The data layer's null rate check
- C. The system layer's error rate

<details><summary>Answer</summary>

**B. The data layer's null rate check**. Green system dashboards can hide broken data

</details>

**4. Score went 81 to 86 after new eval cases. Did the model improve?**

- A. No, new cases only lower scores
- B. Unknown, because the test changed too
- C. Yes, five points is a clear gain

<details><summary>Answer</summary>

**B. Unknown, because the test changed too**. Same ruler, or no comparison

</details>

**5. Your design has no fallback. What does the user see on a timeout?**

- A. An error page in an unrelated flow
- B. A rules baseline answer
- C. A cached prediction, automatically

<details><summary>Answer</summary>

**A. An error page in an unrelated flow**. No plan means the fallback is an error

</details>

## Say it in the interview

**Say it: PSI**

- Symmetric KL, used to rank moved features
- Rules of thumb; small samples inflate PSI
- Baseline alerts; act when it matters

**Say it: diagnosing degradation**

- Real metric first, then the pipeline
- Retrain only when the plumbing is clean
- Segment throughout; monitor freshness too

**Say it: four layers**

- Four layers; failures hide in the middle
- Prediction distributions arrive before labels
- Without proxies, you wait blind for labels

**Say it: retraining**

- Triggers first, calendar as backstop
- A score needs a known eval set version

**Say it: fallback**

- Fallback decides your worst day
- Irreversible means a human; never no plan

## Homework

- [ ] Rerun the PSI lab with twenty bins
- [ ] Write the four-step diagnosis order
- [ ] One check per monitoring layer
- [ ] Sketch a fallback for one model
