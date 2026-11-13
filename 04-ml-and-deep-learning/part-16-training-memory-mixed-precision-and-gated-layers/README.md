# Machine Learning and Deep Learning · Part 16 of 28: Training Memory, Mixed Precision and Gated Layers

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Training memory and gradient checkpointing
2. Mixed precision: fp16, bf16 and FP8
3. Gated activations and normalisation conventions
4. Question drill: Theory corrections

## Key takeaways

- Size beyond parameters; checkpoint to save memory
- Savings depend on regime; bf16 trades precision
- Gated layers and RMSNorm are conventions
- Know where textbook claims break

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_checkpointing_each_block.py` | Checkpointing each block | yes |
| `code/02_autocast_with_a_grad_scaler.py` | Autocast with a grad scaler | yes |
| `code/03_the_scaled_backward_step.py` | The scaled backward step | yes |
| `code/04_lab_size_training_memory_by_hand.py` | Size training memory by hand | yes |
| `code/05_a_swiglu_block_in_pytorch.py` | A SwiGLU block in PyTorch | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/04_lab_size_training_memory_by_hand.py` prints:

```text
fp32 weights: 4 GB
+ grads: 8 GB
+ Adam: 16 GB
fp32+fp16 weights: 6 GB
activations: not counted yet
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. A GPU just fits a model's weights. Can you fine-tune it there with Adam?**

- A. No, gradients, Adam and activations add more
- B. Yes, with a small learning rate
- C. Yes, the weights fit, so it fits

<details><summary>Answer</summary>

**A. No, gradients, Adam and activations add more**. Never size a training GPU from parameters alone

</details>

**2. Does mixed precision halve training memory?**

- A. It depends on the regime
- B. No, it never saves memory
- C. Yes, 16 bits is half of 32

<details><summary>Answer</summary>

**A. It depends on the regime**. Ask which regime, and where the saving comes from

</details>

**3. Is bf16 strictly better than fp16?**

- A. Yes, it has fp32's range
- B. No, it trades precision for range
- C. No, it cannot train big models

<details><summary>Answer</summary>

**B. No, it trades precision for range**. bf16 trades precision for range

</details>

**4. Which gated activation does Gemma use in its feed-forward layers?**

- A. SwiGLU, like every LLM
- B. GeGLU, from the same paper
- C. Plain leaky ReLU

<details><summary>Answer</summary>

**B. GeGLU, from the same paper**. SwiGLU is a family convention, not universal

</details>

**5. Does bias squared plus variance plus noise hold for classification accuracy?**

- A. Yes, it always holds
- B. Only with enough training data
- C. No, it is exact only for squared loss

<details><summary>Answer</summary>

**C. No, it is exact only for squared loss**. The decomposition is exact only for squared loss

</details>

## Say it in the interview

**Training memory, in one answer**

- Training keeps every activation until backprop.
- Parameters are a fraction of training memory.
- Checkpointing: one extra forward, big memory saving.

**Mixed precision, in one answer**

- fp16 needs loss scaling; bf16 keeps fp32's range.
- Master copies add memory; autocast saves activations.
- Big win only when activations dominate.

**Activations, in one answer**

- SwiGLU plus RMSNorm is the LLaMA convention.
- RMSNorm skips mean-centring: cheaper, about as good.
- Batch norm works; its original story was challenged.

## Homework

- [ ] Estimate training memory for one model
- [ ] Add checkpoint to a toy model
- [ ] Write fp16 and bf16 bit layouts
- [ ] Build SwiGLU, then make it GeGLU
