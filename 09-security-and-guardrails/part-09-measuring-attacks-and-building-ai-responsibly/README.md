# Security and Guardrails · Part 9 of 11: Measuring Attacks and Building AI Responsibly

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Attack success rate
2. Responsible AI principles
3. Fairness and bias evaluation
4. Transparency: disclosure, model cards and system cards
5. Red teaming
6. Data minimisation

## Key takeaways

- Report ASR with counts, interval, false blocks
- Principles need tests and owners
- Slice by group, watch for proxies
- Disclose to users, document for reviewers
- Every hit becomes a test
- Collect less, leak less

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_two_rates_from_one_run.py` | Two Rates From One Run | yes |
| `code/02_lab_simulate_an_attack_report.py` | Simulate an Attack Report | yes |
| `code/03_an_allowlist_before_the_prompt.py` | An Allowlist Before the Prompt | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/02_lab_simulate_an_attack_report.py` prints:

```text
attempts: 25
per attempt: 0.16
any of 5: 2 of 5
0 of 20: up to 15%
```

## Try it without a key

- [Gandalf](https://gandalf.lakera.ai): A game: trick a model into revealing a password. The quickest way to feel prompt injection.

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. Your defence blocked all 20 attacks you tried. What can you honestly claim?**

- A. The defence is attack-proof
- B. The attack success rate is exactly zero
- C. The true rate may reach about 15%

<details><summary>Answer</summary>

**C. The true rate may reach about 15%**. Report counts and an interval, not zero

</details>

**2. The interviewer asks how you measure inclusiveness. What is the strongest answer?**

- A. Name a test and an owner for it
- B. Our team deeply values inclusiveness
- C. We follow Microsoft's six principles

<details><summary>Answer</summary>

**A. Name a test and an owner for it**. No test and no owner means a poster

</details>

**3. We never collect gender. Can our system still be biased?**

- A. Only if trained on gender labels
- B. Yes, names and locations act as proxies
- C. No, without gender data it cannot be

<details><summary>Answer</summary>

**B. Yes, names and locations act as proxies**. Missing columns do not remove bias

</details>

**4. What does transparency mean for the users of your AI app?**

- A. Know it is AI, see sources, reach humans
- B. Open source the model weights
- C. Publish every system prompt

<details><summary>Answer</summary>

**A. Know it is AI, see sources, reach humans**. Transparency serves users, not prompt dumps

</details>

**5. You red-teamed before launch. Last week the model was swapped. What now?**

- A. Retest only if users complain
- B. Rerun the attack suite on it
- C. Nothing, launch testing covered it

<details><summary>Answer</summary>

**B. Rerun the attack suite on it**. Red teaming never ends at launch

</details>

**6. We redact everything, so can we safely collect everything?**

- A. Yes, as long as the logs exist
- B. Yes, redaction makes all data safe
- C. No, redactors miss things, so collect less

<details><summary>Answer</summary>

**C. No, redactors miss things, so collect less**. Redaction misses things. Collect less.

</details>

## Say it in the interview

**Say It in the Interview**

- Give the rate, not a claim
- Pair it with the false-block rate
- Counts, interval, held-out set

**Say It in the Interview**

- Every principle becomes something testable
- Sliced evals, owners, audit trails
- No test, no owner: a poster

**Say It in the Interview**

- Averages hide badly served groups
- Guardrails often over-block dialects
- Fix the gap, keep the slice

**Say It in the Interview**

- A user side and a reviewer side
- Purpose, data, evals, failures, owner
- A short, versioned system card

**Say It in the Interview**

- Attack it before an adversary does
- Automated variants plus human creativity
- Every hit becomes a regression test

**Say It in the Interview**

- Never collected means never leaked
- IDs and redacted text, not raw prompts
- It shrinks every failure's blast radius

## Homework

- [ ] Run the lab with a new seed
- [ ] Rule of three for 50 trials
- [ ] One principle: write its test, owner
- [ ] Write an allowlist for one form
