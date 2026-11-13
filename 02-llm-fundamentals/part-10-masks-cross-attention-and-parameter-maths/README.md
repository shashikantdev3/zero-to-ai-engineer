# LLM Fundamentals · Part 10 of 18: Masks, Cross-Attention and Parameter Maths

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Masking: causal versus padding
2. Cross-attention
3. Attention weights are not explanations
4. SwiGLU and transformer parameter maths

## Key takeaways

- Big negative on scores; finite for padding
- Decoder queries, encoder keys and values
- Heat maps are not explanations
- Feed-forward holds most parameters

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_combining_causal_and_padding_masks.py` | Combining causal and padding masks | yes |
| `code/02_lab_softmax_with_and_without_masks.py` | Softmax with and without masks | yes |
| `code/03_cross_attention_in_numpy.py` | Cross-attention in NumPy | yes |
| `code/04_counting_a_llama_3_8b_style_layer.py` | Counting a Llama 3 8B style layer | yes |
| `code/05_swiglu_in_a_few_lines.py` | SwiGLU in a few lines | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/02_lab_softmax_with_and_without_masks.py` prints:

```text
raw: [0.63, 0.23, 0.14]
zero: [0.67, 0.24, 0.09]
finite: [0.73, 0.27, 0.0]
empty: [0.5, 0.5]
inf row: [nan, nan]
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. To block a token in attention, what do you set?**

- A. A very negative score, before softmax
- B. Zero weight after softmax, no renormalising
- C. A zero score, before softmax

<details><summary>Answer</summary>

**A. A very negative score, before softmax**. Mask scores with a big negative, before softmax

</details>

**2. Does cross-attention need a causal mask over the source?**

- A. Yes, to hide future source tokens
- B. Only during training
- C. No, the source is fully visible

<details><summary>Answer</summary>

**C. No, the source is fully visible**. Causal mask: decoder self-attention only

</details>

**3. A heat map shows strong weight on one sentence. Is the answer grounded?**

- A. Yes, the heat map proves it
- B. Not proven; check the cited source
- C. Yes, if that head's weight is high

<details><summary>Answer</summary>

**B. Not proven; check the cited source**. A heat map is not evidence of grounding

</details>

**4. Which part holds most of a modern transformer layer's parameters?**

- A. The feed-forward block
- B. The attention block
- C. The output projection alone

<details><summary>Answer</summary>

**A. The feed-forward block**. Most parameters sit in the feed-forward block

</details>

## Say it in the interview

**Masking in the interview**

- Mask scores before softmax, very negative
- Causal rows always keep the diagonal
- Padding: finite negative, or drop those rows

**Cross-attention in the interview**

- One sequence looking at another
- Output attends to the full source
- Encoder side once; decoder cache grows

**Heat maps in the interview**

- Weighted average, not a spotlight
- Change the weights, keep the prediction
- Rely on citations you can verify

**Parameter maths in the interview**

- A gate branch multiplies the main branch
- Three matrices, so a smaller hidden size
- Most of the model is not attention

## Homework

- [ ] Break and fix a padding row
- [ ] Run cross-attention with three queries, five keys
- [ ] Recount with full attention, plain 4d MLP
- [ ] Explain why causal rows never go NaN
