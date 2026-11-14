# Evaluation · Part 11 of 11: Knowing When the Model Is Guessing

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Uncertainty signals: self-consistency, SelfCheckGPT, semantic entropy
2. Abstain: the refusal path
3. Risk-tiered review
4. Judge prompt injection

## Key takeaways

- Scattered samples mean the model is guessing
- Design refusal; test refusing and over-refusing
- Code sets the tier; unknown goes to humans
- Fence graded text and attack your judge

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_normalise_then_sample.py` | Normalise, Then Sample | yes |
| `code/02_majority_vote_and_agreement_score.py` | Majority Vote and Agreement Score | yes |
| `code/03_measuring_refusal_both_ways.py` | Measuring Refusal Both Ways | yes |
| `code/04_tiers_and_explicit_lists.py` | Tiers and Explicit Lists | yes |
| `code/05_the_default_deny_router.py` | The Default-Deny Router | yes |
| `code/06_lab_lab_test_the_router.py` | Lab: Test the Router | yes |
| `code/07_rubric_outside_attacks_ready.py` | Rubric Outside, Attacks Ready | yes |
| `code/08_building_the_fenced_prompt.py` | Building the Fenced Prompt | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/06_lab_lab_test_the_router.py` prints:

```text
faq_general -> send_with_citations
faq_general -> human_review
payout_v2 -> human_review
payout_request -> human_review
```

## Try it without a key

- [Google AI Studio](https://aistudio.google.com): A real model with temperature, top-p, thinking level and output length controls. Needs a Google account, no credit card. Do not paste private data: free-tier prompts may be used to improve Google products.
- [Gandalf](https://gandalf.lakera.ai): A game: trick a model into revealing a password. The quickest way to feel prompt injection.

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. The model says it is 95% confident. Can you threshold that score?**

- A. Only after checking calibration on labels
- B. Yes, if temperature is zero
- C. Yes, high confidence means it is right

<details><summary>Answer</summary>

**A. Only after checking calibration on labels**. Plot stated confidence against actual accuracy first

</details>

**2. Your prompt says 'if unsure, say you do not know'. Is that enough?**

- A. Yes, the instruction handles it
- B. No, measure both refusal rates
- C. Yes, if the model is large

<details><summary>Answer</summary>

**B. No, measure both refusal rates**. Measure correct refusals and over-refusals

</details>

**3. A model labels the intent, and the router trusts that label. What's the risk?**

- A. None, the label is deterministic
- B. Routing just gets slower
- C. A payout could land in the low tier

<details><summary>Answer</summary>

**C. A payout could land in the low tier**. A model label must never lower the tier

</details>

**4. Someone adds a new workflow called payout_v2. Which tier does it land in?**

- A. Whatever the model's confidence says
- B. Human review, because it is unknown
- C. Low tier, as the fallback

<details><summary>Answer</summary>

**B. Human review, because it is unknown**. Unknown workflows default to human review

</details>

**5. Your answer model learned that addressing the grader raises its score. How would you notice?**

- A. Attack cases asserting the verdict holds
- B. You can't; the judge only grades
- C. Give the judge a longer rubric

<details><summary>Answer</summary>

**A. Attack cases asserting the verdict holds**. If attacks flip the verdict, the judge cannot gate

</details>

## Say it in the interview

**Uncertainty in the Interview**

- Agreement across samples, no reference needed
- Several calls per answer: use on high-risk routes
- Self-reported confidence needs calibration first

**Refusal in the Interview**

- Make I do not know an available answer
- Say what is missing, offer a person
- Refusing everything is safe and useless

**Risk Tiers in the Interview**

- The tier comes from code, not the model
- Default deny; a model may only raise tiers
- The model drafts; it does not adjudicate

**Judge Injection in the Interview**

- A judge reads untrusted text, so it can be injected
- Fence the data, separate the rubric, test the judge
- Code does not read instructions

## Homework

- [ ] Run self-consistency on short questions
- [ ] Write two must-refuse and two answerable cases
- [ ] Add a new workflow and check its tier
- [ ] Write one judge attack case
