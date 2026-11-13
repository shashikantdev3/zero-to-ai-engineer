# LLM Fundamentals · Part 7 of 18: Inside the Transformer: Masks, Heads, Positions

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Causal mask and decoder-only models
2. Encoder, decoder and encoder-decoder
3. Multi-head attention
4. Positional encoding and RoPE

## Key takeaways

- Causal mask hides the future
- Encoders understand, decoders generate
- Several heads, roughly one head's cost
- Positions give order, RoPE encodes distance

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_building_the_mask_in_numpy.py` | Building the mask in NumPy | yes |
| `code/02_lab_a_causal_mask_in_plain_python.py` | A causal mask in plain Python | yes |
| `code/03_multi_head_attention_in_numpy.py` | Multi-head attention in NumPy | yes |
| `code/04_sinusoidal_encoding_in_numpy.py` | Sinusoidal encoding in NumPy | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/02_lab_a_causal_mask_in_plain_python.py` prints:

```text
[0, 1, 1, 1]
[0, 0, 1, 1]
[0, 0, 0, 1]
[0, 0, 0, 0]
[0.73, 0.27, 0.0, 0.0]
```

## Try it without a key

- [Transformer Explainer](https://poloclub.github.io/transformer-explainer/): A small GPT-2 running in your browser. Type a prompt, move the temperature slider and watch the next-token probabilities change. Free, no account.
- [LLM Visualization](https://bbycroft.net/llm): A 3D walkthrough of every step inside a tiny GPT. Free, no account.

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. Which transformer design do most chat LLMs use?**

- A. Decoder-only with a causal mask
- B. The full encoder-decoder transformer
- C. Encoder-only, like BERT

<details><summary>Answer</summary>

**A. Decoder-only with a causal mask**. Chat models are decoder-only with a causal mask

</details>

**2. Is BERT just a smaller GPT?**

- A. No, it reads both ways to understand
- B. Yes, but trained on less text
- C. Yes, same design with fewer layers

<details><summary>Answer</summary>

**A. No, it reads both ways to understand**. Different family, different job

</details>

**3. If head size = d_model / h, do more heads mean more compute?**

- A. Yes, parameters double each time
- B. Yes, compute grows with every head
- C. No, cost stays roughly the same

<details><summary>Answer</summary>

**C. No, cost stays roughly the same**. Smaller heads keep total cost flat

</details>

**4. Does a model know word order because it reads left to right?**

- A. Yes, softmax keeps the order
- B. No, attention alone is order-blind
- C. Yes, it reads tokens left to right

<details><summary>Answer</summary>

**B. No, attention alone is order-blind**. Without positions, attention is order-blind

</details>

## Say it in the interview

**Causal mask**

- Decoder-only, each token sees only the past
- Minus infinity before softmax, one-pass training
- Fixed past tokens make the KV cache possible

**Three families**

- Encoder-only understands
- Encoder-decoder translates, decoder-only continues
- Decoder-only scales: text in, text out

**Multi-head**

- Several heads, each a slice of d_model
- Several views for roughly the same price
- Heads specialise, but not always neatly

**Positions**

- No positions means no word order
- RoPE: score depends on token distance
- Rescale RoPE, but test the new length

## Homework

- [ ] Run the mask lab with n set to 6
- [ ] Sketch the three families and their uses
- [ ] Compute head size: 512 dims, 8 heads
- [ ] Explain RoPE in two sentences
