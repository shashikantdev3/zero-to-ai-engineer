# LLM Fundamentals · Part 6 of 18: Inside the Transformer: How Attention Works

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Why transformers replaced RNNs and LSTMs
2. Self-attention
3. Query, key and value
4. Scaled dot-product attention and its quadratic cost

## Key takeaways

- Attention: parallel training, one-step paths
- Each token: weighted mix of visible tokens
- Query matches key; value gets sent
- Scale for gradients; scores cost n squared

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_self_attention_in_numpy.py` | Self-attention in NumPy | yes |
| `code/02_lab_scaling_and_squares_in_python.py` | Scaling and squares in Python | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/02_lab_scaling_and_squares_in_python.py` prints:

```text
raw: [1.0, 0.0, 0.0]
scaled: [0.665, 0.245, 0.09]
8000 tokens: 64000000 scores
16000 tokens: 256000000 scores
```

## Try it without a key

- [Transformer Explainer](https://poloclub.github.io/transformer-explainer/): A small GPT-2 running in your browser. Type a prompt, move the temperature slider and watch the next-token probabilities change. Free, no account.
- [LLM Visualization](https://bbycroft.net/llm): A 3D walkthrough of every step inside a tiny GPT. Free, no account.

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. What does an RNN do better than a transformer at inference?**

- A. Learns long-range links more easily
- B. Keeps a fixed-size state per step
- C. Trains faster in parallel

<details><summary>Answer</summary>

**B. Keeps a fixed-size state per step**. RNN state stays fixed; the KV cache keeps growing

</details>

**2. Where does an LLM's memory of earlier chat turns actually live?**

- A. In the history resent each request
- B. In a hidden state the API keeps
- C. In attention weights between requests

<details><summary>Answer</summary>

**A. In the history resent each request**. Attention only sees the current context

</details>

**3. In self-attention, where do Q, K and V come from?**

- A. Queries from encoder, the rest decoder
- B. All from the same tokens
- C. Three separate input sequences

<details><summary>Answer</summary>

**B. All from the same tokens**. Self-attention: Q, K, V from the same tokens

</details>

**4. Is FlashAttention an approximation of attention?**

- A. Yes, it skips low-weight scores
- B. Yes, it makes attention linear
- C. No, it gives the exact result

<details><summary>Answer</summary>

**C. No, it gives the exact result**. Exact result; speed from fewer memory reads and writes

</details>

**5. Doubling a prompt from 8,000 to 16,000 tokens does what to TTFT?**

- A. Roughly doubles it
- B. Exactly quadruples it
- C. Leaves it about the same

<details><summary>Answer</summary>

**A. Roughly doubles it**. Only the attention term quadruples

</details>

## Say it in the interview

**Why transformers won**

- One token at a time, one hidden state
- Slow training, weak long-range learning
- Parallel and short paths, but quadratic cost

**Explaining self-attention**

- Every word asks which words help it
- Score, weight, blend, for every word
- Projections, dot product, softmax, weighted sum

**Explaining query, key and value**

- Query, labels, contents: it is search
- Dot product picks where to look
- Relevance is not the same as content

**Explaining scaled attention**

- Scale so softmax does not go one-hot
- n by n scores: quadratic in context
- FlashAttention: exact, faster, still quadratic

## Homework

- [ ] Sketch RNN and attention paths for five tokens
- [ ] Write every attention shape from memory
- [ ] Rerun the lab with a bigger d_k
- [ ] Explain why KV cache grows but RNN state stays
