# Machine Learning and Deep Learning · Part 15 of 28: Losses, Warmup, Saddles and NaN Debugging

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Losses as maximum likelihood, and why cross-entropy beats MSE for classification
2. Contrastive and triplet losses
3. Learning-rate warmup: why, honestly
4. Non-convexity and saddle points
5. Loss is NaN: the debug order

## Key takeaways

- Cross-entropy learns fastest from its worst mistakes.
- Your positive pairs define what similar means.
- Warmup's reason is unsettled. Architecture matters.
- Plateau? Check schedule and momentum before minima.
- NaN: when, then data, rate, arithmetic.

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_two_gradients_one_wrong_prediction.py` | Two gradients, one wrong prediction | yes |
| `code/02_lab_gradients_across_three_logits.py` | Gradients across three logits | yes |
| `code/03_triplet_margin_loss_in_pytorch.py` | Triplet margin loss in PyTorch | yes |
| `code/04_linear_warmup_into_cosine_decay.py` | Linear warmup into cosine decay | yes |
| `code/05_three_nan_debugging_tools.py` | Three NaN debugging tools | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/02_lab_gradients_across_three_logits.py` prints:

```text
z -6 ce -0.998 mse -0.005
z -2 ce -0.881 mse -0.185
z +2 ce -0.119 mse -0.025
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. A sigmoid classifier is confidently wrong. What does the MSE gradient do?**

- A. It equals p minus y
- B. It almost vanishes
- C. It becomes very large

<details><summary>Answer</summary>

**B. It almost vanishes**. A saturated sigmoid kills the squared error gradient.

</details>

**2. Two sentences have cosine similarity 0.9. What can you conclude?**

- A. They are paraphrases of each other
- B. They are close under this model's training
- C. They agree with each other

<details><summary>Answer</summary>

**B. They are close under this model's training**. Similarity reflects the training objective, not agreement.

</details>

**3. If early gradients were simply large, why would pre-LN models need less warmup?**

- A. Warmup partly compensated for post-LN design
- B. Pre-LN early gradients are even larger
- C. Pre-LN models never use Adam

<details><summary>Answer</summary>

**A. Warmup partly compensated for post-LN design**. Architecture matters. The folk reason is not the answer.

</details>

**4. Training stalls on a plateau. What do you check first?**

- A. Learning-rate schedule and momentum
- B. Nothing, it is a local minimum
- C. Swap in a new architecture

<details><summary>Answer</summary>

**A. Learning-rate schedule and momentum**. Rule out a saddle or small rate first.

</details>

**5. Loss is NaN at step 1. Where do you look first?**

- A. Lower the learning rate until it stops
- B. Switch to a different optimiser
- C. The input batch and initialisation

<details><summary>Answer</summary>

**C. The input batch and initialisation**. Check the input batch where NaN first appeared.

</details>

## Say it in the interview

**Cross-entropy versus squared error**

- The loss should match the target's distribution.
- Squared error barely learns from its worst mistakes.
- Cross-entropy learns fastest where it is most wrong.

**How embedding models learn**

- Pull anchor to positive, push from negative.
- Random negatives are too easy. Mine hard ones.
- I evaluate embedding models on my own queries.

**Why warmup, honestly**

- Early gradients are large is folklore.
- Noisy Adam estimate, or post-layer-norm architecture.
- Linear warmup, cosine decay, AdamW.

**Non-convexity in practice**

- Non-linearities plus symmetry mean no guarantees.
- In high dimensions, saddles are the usual trouble.
- Convex: optimiser changes speed, not the answer.

**How I debug a NaN loss**

- Step one NaN: check data and initialisation.
- Later NaN: lower the rate, clip, find the arithmetic.
- Never paper over a data problem.

## Homework

- [ ] Rerun the lab with a logit of minus 10.
- [ ] Write two sentences on hard negatives.
- [ ] Write both warmup mechanisms from memory.
- [ ] Write the NaN debug order as a checklist.
