# Machine Learning and Deep Learning · Part 23 of 28: Fine-Tuning Facts, Design Rounds, Clean A/B Tests

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Can fine-tuning teach facts? The scoped answer
2. Question drill: Production ML
3. The ML system design round
4. A/B test design
5. Peeking

## Key takeaways

- Facts in retrieval; raw-text fine-tuning is weak
- Diagnose first; always pass the eval gate
- The decision fixes everything downstream
- Decide in advance; randomise by user
- No decisions on interim p-values

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_lab_hash_users_into_variants.py` | Hash users into variants | yes |
| `code/02_simulating_peeking_on_a_a_tests.py` | Simulating peeking on A/A tests | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/01_lab_hash_users_into_variants.py` prints:

```text
u1 A
u2 B
u3 A
again: A
A share: 0.5084
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. Does the cited study show fine-tuning can never teach facts?**

- A. No, it only tested raw-text training
- B. Yes, retrieval won on every kind of fact
- C. Yes, weights cannot hold new facts

<details><summary>Answer</summary>

**A. No, it only tested raw-text training**. Raw-text fine-tuning is weak, not hopeless

</details>

**2. Accuracy dropped. Should you just retrain on recent data?**

- A. No, diagnose first, then pass the eval gate
- B. Yes, but only on the last week
- C. Yes, fresh data fixes most drops

<details><summary>Answer</summary>

**A. No, diagnose first, then pass the eval gate**. Diagnose first; every retrain passes the gate

</details>

**3. First minute of the design round. What do you say first?**

- A. Which features I would build
- B. What decision the output drives
- C. I would use a transformer

<details><summary>Answer</summary>

**B. What decision the output drives**. Frame the decision before naming any model

</details>

**4. You assign prompt variants per request. What goes wrong?**

- A. The sample size gets too small
- B. Nothing, requests are more independent
- C. One user gets both prompts in a chat

<details><summary>Answer</summary>

**C. One user gets both prompts in a chat**. Randomise by user, so nobody sees both

</details>

**5. "We stopped early because it was clearly significant." Valid?**

- A. Yes, a clear result cannot be noise
- B. Not yet, ask how many times they looked
- C. Yes, if the p-value was very small

<details><summary>Answer</summary>

**B. Not yet, ask how many times they looked**. Ask how many times they looked

</details>

## Say it in the interview

**Say it in the interview**

- Facts in retrieval, behaviour in weights
- Raw-text fine-tuning is a poor knowledge tool
- Retrieval wins on freshness and citations

**Say it in the interview**

- Start with the decision, not the model
- The model has to beat a baseline
- Simple first, complex once the gap shows

**Say it in the interview**

- Decide everything before the data
- By user, in full weeks
- A clean canary says nothing about better

**Say it in the interview**

- Daily checks, stop at first dip
- Every look is another lottery ticket
- Fixed horizon, or a sequential method

## Homework

- [ ] Write the scoped fine-tuning claim
- [ ] Frame fraud detection: decision, label, baseline
- [ ] Run the hashing lab with your IDs
- [ ] Rerun peeking with five peeks
