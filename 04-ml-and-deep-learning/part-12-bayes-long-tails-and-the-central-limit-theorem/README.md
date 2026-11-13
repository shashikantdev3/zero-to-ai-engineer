# Machine Learning and Deep Learning · Part 12 of 28: Bayes, Long Tails and the Central Limit Theorem

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Bayes' theorem and the base-rate trap
2. Discriminative versus generative models
3. Distributions and long tails
4. Central limit theorem

## Key takeaways

- Rare condition: the prior dominates, so count people
- Discriminative: P(Y|X). Generative: P(X, Y).
- Long tails: report percentiles, not the mean
- CLT covers means; bootstrap percentiles

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_the_posterior_in_code.py` | The posterior in code | yes |
| `code/02_naive_bayes_versus_logistic_regression.py` | Naive Bayes versus logistic regression | yes |
| `code/03_skewed_latency_mean_versus_median.py` | Skewed latency, mean versus median | yes |
| `code/04_lab_mean_versus_percentiles_by_hand.py` | Mean versus percentiles, by hand | yes |
| `code/05_averaging_skewed_data.py` | Averaging skewed data | yes |
| `code/06_bootstrapping_a_p99.py` | Bootstrapping a p99 | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/04_lab_mean_versus_percentiles_by_hand.py` prints:

```text
median      49.4 ms
mean        68.1 ms
p95        185.7 ms
p99        315.1 ms
mean+2sd   195.9 ms
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. A 99% accurate test, prevalence 1 in 10,000. You test positive. Chance you are sick?**

- A. About 1 percent
- B. About 99 percent
- C. About 50 percent

<details><summary>Answer</summary>

**A. About 1 percent**. The prior does the work, not the accuracy

</details>

**2. In classic ML, what does a generative model learn?**

- A. How to write new text
- B. The joint probability of X and Y
- C. Only the decision boundary

<details><summary>Answer</summary>

**B. The joint probability of X and Y**. Generative means modelling P(X, Y), not writing text

</details>

**3. You call latency normal and quote mean ± 2 SD. Why is p99 far outside?**

- A. Latency is long-tailed, not normal
- B. The p99 was computed wrong
- C. Too few requests were measured

<details><summary>Answer</summary>

**A. Latency is long-tailed, not normal**. Skewed data: quote percentiles, not mean plus two SD

</details>

**4. You used a normal-theory interval for a p99 difference. What went wrong?**

- A. Nothing, the CLT covers p99
- B. The sample means were not normal
- C. The interval came out far too narrow

<details><summary>Answer</summary>

**C. The interval came out far too narrow**. CLT covers means, not percentiles: bootstrap p99

</details>

## Say it in the interview

**Say it in the interview**

- First, pin down what accurate means
- One real case against a hundred false ones
- Rare class: precision collapses despite good recall

**Say it in the interview**

- Discriminative: P(Y|X). Generative: P(X, Y) plus Bayes.
- The trade-off is data size
- Naive Bayes: useful ranking, overconfident probabilities

**Say it in the interview**

- Long-tailed data: report median, p95, p99
- A mean of 80 ms can hide 4-second waits
- p99s do not add across services

**Say it in the interview**

- Averages are normal even when data is not
- Four times the traffic halves the interval
- For p95 or p99, I bootstrap

## Homework

- [ ] Rerun Bayes with prevalence 1 in 100
- [ ] Change sigma in the lab; compare mean and median
- [ ] Compare both models at several training sizes
- [ ] Write the four interview answers yourself
