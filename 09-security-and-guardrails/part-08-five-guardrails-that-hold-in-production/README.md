# Security and Guardrails · Part 8 of 11: Five Guardrails That Hold in Production

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. PII detection and redaction
2. Groundedness checking
3. Per-category thresholds and error cost
4. Shadow mode, labelled traffic and appeals
5. Guardrail latency and cost

## Key takeaways

- Redact before, after, and always in logs
- Exists and supports are two checks
- One threshold per category, set by cost
- Shadow first, labels from review and appeals
- Cheap first, parallel, expensive only where risky

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_redaction_with_microsoft_presidio.py` | Redaction with Microsoft Presidio | after `pip install presidio_analyzer presidio_anonymizer` |
| `code/02_quote_checker_the_rules.py` | Quote checker: the rules | yes |
| `code/03_quote_checker_the_check.py` | Quote checker: the check | yes |
| `code/04_per_category_config.py` | Per-category config | yes |
| `code/05_lab_choose_a_threshold_by_cost.py` | Choose a threshold by cost | yes |
| `code/06_logging_a_shadow_decision.py` | Logging a shadow decision | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/05_lab_choose_a_threshold_by_cost.py` prints:

```text
block_at 2: fb=3 miss=0 cost=3
block_at 4: fb=1 miss=1 cost=11
block_at 6: fb=0 miss=2 cost=20
choose block_at 2
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. Your system prompt says 'never share personal data', in bold. What enforces it?**

- A. The bold text makes the model obey
- B. Nothing, you need real redaction
- C. The model's safety training is enough

<details><summary>Answer</summary>

**B. Nothing, you need real redaction**. A prompt is a request. Redaction is a control.

</details>

**2. Every claim in an answer has a citation. Does that prove the answer is right?**

- A. Yes, citations prove correctness
- B. No, the passage must support it
- C. Yes, if the source is trusted

<details><summary>Answer</summary>

**B. No, the passage must support it**. Citations show where, not whether it is true

</details>

**3. Should you set every category to its strictest threshold, safety first?**

- A. No, it blocks too many good users
- B. Yes, safety always comes first
- C. Yes, false blocks cost nothing

<details><summary>Answer</summary>

**A. No, it blocks too many good users**. False blocks are a cost, not free safety

</details>

**4. Customers complain about blocks. Should you loosen the guardrail until complaints stop?**

- A. No, measure the misses too
- B. Yes, fewer blocks means happier users
- C. Yes, complaints are the only signal

<details><summary>Answer</summary>

**A. No, measure the misses too**. Complaints show false blocks, never the misses

</details>

**5. You stream a reply and retract it on a hit. What about tokens already shown?**

- A. They vanish before anyone reads them
- B. The provider always holds them back
- C. The user may have already seen them

<details><summary>Answer</summary>

**C. The user may have already seen them**. Retracting is too late for high-risk text

</details>

## Say it in the interview

**Interview answer: PII redaction**

- Before, after, and always in logs
- Patterns, checksums and an entity model
- Measure recall. Pair it with data minimisation.

**Interview answer: groundedness**

- Quote it, name it, verify it verbatim
- Exists and supports are separate checks
- I do not know must be available

**Interview answer: thresholds**

- One global threshold is almost always wrong
- Count errors, weight by cost, choose
- Thresholds go through review like code

**Interview answer: shadow mode**

- Tune with data, not opinions
- Labels from review and appeals
- Shadow first, enforce when better

**Interview answer: latency and cost**

- Layer guardrails by price
- Buffer on high risk, retract on low
- Track guardrail latency as its own span

## Homework

- [ ] Write a Luhn check for card numbers
- [ ] Test the quote checker on edge cases
- [ ] Rerun the lab with a cheaper miss
- [ ] Map redaction points in one system
