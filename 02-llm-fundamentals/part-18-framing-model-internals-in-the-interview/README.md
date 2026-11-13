# LLM Fundamentals · Part 18 of 18: Framing Model Internals in the Interview

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Placing your internals depth
2. The three-minute attention whiteboard
3. One current point after the answer
4. Question drill: Internals framing
5. Perplexity

## Key takeaways

- Say early: explained, built, or trained
- Q, K, V, scale, mask, softmax, sum
- Answer first, one current fact, stop
- Ask the recruiter what each round covers
- Perplexity: prediction, not truth or helpfulness

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_checking_the_softmax_gradient.py` | Checking the Softmax Gradient | yes |
| `code/02_perplexity_in_three_lines.py` | Perplexity in Three Lines | yes |
| `code/03_lab_perplexity_by_hand.py` | Perplexity by Hand | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/03_lab_perplexity_by_hand.py` prints:

```text
mean NLL: 1.35
perplexity: 3.86
uniform over 10: 10.00
confident model: 1.01
```

## Try it without a key

- [Transformer Explainer](https://poloclub.github.io/transformer-explainer/): A small GPT-2 running in your browser. Type a prompt, move the temperature slider and watch the next-token probabilities change. Free, no account.

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. With cross-entropy, what is the gradient with respect to the logits?**

- A. minus log of p
- B. p minus the one-hot target
- C. p times one minus p

<details><summary>Answer</summary>

**B. p minus the one-hot target**. Don't bluff, don't under-sell: gradient is p minus y

</details>

**2. Before softmax, what value does the causal mask put on future positions?**

- A. Minus infinity
- B. One
- C. Zero

<details><summary>Answer</summary>

**A. Minus infinity**. Mask with minus infinity, and never skip the scaling

</details>

**3. Where should a current 2026 fact go in your answer?**

- A. Instead of the explanation
- B. As your opening line
- C. After a full, correct explanation

<details><summary>Answer</summary>

**C. After a full, correct explanation**. Mechanism first; currency is the dessert

</details>

**4. On the whiteboard, how do you turn MHA into GQA?**

- A. Fewer K and V heads, repeated per group
- B. Fewer query heads sharing one key
- C. Remove the output projection

<details><summary>Answer</summary>

**A. Fewer K and V heads, repeated per group**. Shrink K and V heads; keep every query head

</details>

**5. Model A has lower perplexity than B, with a different tokenizer. Is A the better assistant?**

- A. Yes, lower perplexity is better
- B. Perplexity cannot tell you that
- C. Only if the gap is large

<details><summary>Answer</summary>

**B. Perplexity cannot tell you that**. Perplexity doesn't rank assistants

</details>

## Say it in the interview

**Placing Your Depth, Out Front**

- Production systems: operated and measured
- Internals as mechanism, not from-scratch code
- I'll reason it out, not recite it

**The Whiteboard Answer**

- Scale by √d_k, or softmax saturates
- n by n scores; KV cache holds past K, V
- Drill follow-ups: batch, padding, GQA

**One Current Point, Then Stop**

- Explain properly, then one current point
- Stop, and let them choose the depth

**Explaining Perplexity Well**

- exp of average cross-entropy per token
- Fluent and wrong can still score low
- For products, measure task success with evals

## Homework

- [ ] Write your three-sentence depth statement
- [ ] Draw attention in three minutes, timed
- [ ] One checked current line per topic
- [ ] Rerun the lab with new logprobs
