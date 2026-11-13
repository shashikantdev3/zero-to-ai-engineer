# LLM Fundamentals · Part 2 of 18: Chat Templates, Logits and Training Stages

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Special tokens and chat templates
2. Token embeddings and the output layer
3. Logits, softmax and logprobs
4. Training stages: pretraining, instruction tuning, preference tuning

## Key takeaways

- One stream, role markers, model's own template
- Lookup in, one score per token out
- Logprobs show confidence, not truth
- Facts in retrieval, behaviour in weights

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_see_the_real_role_markers.py` | See the Real Role Markers | yes |
| `code/02_from_token_ids_to_logits.py` | From Token IDs to Logits | yes |
| `code/03_label_confidence_simulated.py` | Label Confidence, Simulated | yes |
| `code/04_lab_break_softmax_then_fix_it.py` | Break Softmax, Then Fix It | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/04_lab_break_softmax_then_fix_it.py` prints:

```text
naive softmax: overflow
probs [0.665, 0.245, 0.09]
sum 1.0
loss 0.408
```

## Try it without a key

- [Tiktokenizer](https://tiktokenizer.vercel.app): Token counts for several models side by side. Free, no account.
- [Transformer Explainer](https://poloclub.github.io/transformer-explainer/): A small GPT-2 running in your browser. Type a prompt, move the temperature slider and watch the next-token probabilities change. Free, no account.

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. Is the system prompt a separate, protected channel?**

- A. Only when the API is hosted
- B. Yes, it is a sealed channel
- C. No, it is markers in one stream

<details><summary>Answer</summary>

**C. No, it is markers in one stream**. Roles are markers, not a security boundary

</details>

**2. Are vector database embeddings the chat model's internal embeddings?**

- A. No, they come from a dedicated model
- B. Only if the weights are tied
- C. Yes, they are the same vectors

<details><summary>Answer</summary>

**A. No, they come from a dedicated model**. Search vectors come from a dedicated model

</details>

**3. Does a high logprob mean the answer is correct?**

- A. Yes, it works as a truth score
- B. No, it measures likelihood, not truth
- C. Only for very short answers

<details><summary>Answer</summary>

**B. No, it measures likelihood, not truth**. High logprob is confidence, not correctness

</details>

**4. Should you fine-tune on your PDFs so the model knows your policies?**

- A. No, put policies in a retrieval index
- B. Yes, and retrain it every month
- C. Yes, fine-tuning adds facts best

<details><summary>Answer</summary>

**A. No, put policies in a retrieval index**. Changing facts go in retrieval, not weights

</details>

## Say it in the interview

**Chat Templates in the Interview**

- Messages become one stream with role markers.
- Wrong template: weaker output, no error.
- Roles help, but they are not security.

**Embeddings in the Interview**

- ID in, learned vector out.
- One score per possible next token.
- Search uses a dedicated embedding model.

**Logprobs in the Interview**

- Softmax gives probabilities. Loss is cross-entropy.
- Low-margin labels go to a human.
- Not a truth score. Check evidence.

**Training Stages in the Interview**

- Pretrain, instruction tune, preference tune.
- Reasoning: rewards from checkable outcomes.
- Facts in retrieval, behaviour in weights.

## Homework

- [ ] Print a chat template, find the markers
- [ ] Break softmax, then fix it
- [ ] Explain logits to logprobs in three sentences
- [ ] Name one fact that belongs in retrieval
