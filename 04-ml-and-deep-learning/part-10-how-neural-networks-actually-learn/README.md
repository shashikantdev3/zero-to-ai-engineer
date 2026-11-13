# Machine Learning and Deep Learning · Part 10 of 28: How Neural Networks Actually Learn

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Activation functions
2. Backpropagation
3. Vanishing and exploding gradients
4. Batch normalisation and layer normalisation
5. Logits and softmax

## Key takeaways

- Activations make depth useful; output follows the task
- Backprop computes gradients; the optimiser uses them
- Residuals, norms, init and clipping keep gradients healthy
- Transformers use layer norm, not batch norm
- Softmax confidence is not correctness

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_activations_and_the_output_rule.py` | Activations and the output rule | yes |
| `code/02_backprop_on_a_single_weight.py` | Backprop on a single weight | yes |
| `code/03_backward_clip_then_step.py` | Backward, clip, then step | yes |
| `code/04_lab_multiply_a_gradient_twenty_times.py` | Multiply a gradient twenty times | yes |
| `code/05_both_layers_in_pytorch.py` | Both layers in PyTorch | yes |
| `code/06_softmax_with_a_temperature.py` | Softmax with a temperature | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/04_lab_multiply_a_gradient_twenty_times.py` prints:

```text
vanishing: 0.0000010
exploding: 3325.3
clipped: 1.0
5 layers: 0.03125
```

## Try it without a key

- [Transformer Explainer](https://poloclub.github.io/transformer-explainer/): A small GPT-2 running in your browser. Type a prompt, move the temperature slider and watch the next-token probabilities change. Free, no account.

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. Why are all your binary probabilities between 0.5 and 0.73?**

- A. The learning rate is too high
- B. A sigmoid was applied twice
- C. The dataset is perfectly balanced

<details><summary>Answer</summary>

**B. A sigmoid was applied twice**. BCEWithLogitsLoss already applies sigmoid. Do not add one.

</details>

**2. Is backpropagation the same thing as the optimiser?**

- A. Yes, it updates the weights itself
- B. Yes, Adam is a kind of backprop
- C. No, it only computes the gradients

<details><summary>Answer</summary>

**C. No, it only computes the gradients**. Backprop computes gradients. The optimiser uses them.

</details>

**3. Gradients vanish in early layers. Should you just raise the learning rate?**

- A. No, the later layers would diverge
- B. Yes, but only with sigmoid
- C. Yes, it boosts the early layers

<details><summary>Answer</summary>

**A. No, the later layers would diverge**. A bigger learning rate makes later layers diverge

</details>

**4. Which normalisation do transformer blocks use?**

- A. No normalisation at all
- B. Layer norm, or RMS norm
- C. Batch norm, like most CNNs

<details><summary>Answer</summary>

**B. Layer norm, or RMS norm**. Transformers use layer norm, not batch norm

</details>

**5. Your model says 0.99 on a wrong answer. How?**

- A. Softmax confidence is not calibration
- B. The logits summed to more than one
- C. Softmax itself must be broken

<details><summary>Answer</summary>

**A. Softmax confidence is not calibration**. High softmax confidence is not correctness

</details>

## Say it in the interview

**Say it: activation functions**

- Activations add the non-linearity that makes depth useful
- ReLU fixed saturation; transformers use GELU-style
- The output activation follows the task

**Say it: backpropagation**

- Backprop is the chain rule, applied efficiently
- Each layer multiplies by its local derivative
- Stored activations: training needs more memory

**Say it: vanishing and exploding**

- Below one it fades; above one it explodes
- ReLU, scaled init, norm layers, residuals, clipping
- Residual plus layer norm: every transformer block

**Say it: normalisation layers**

- Both keep activations in a healthy range
- Batch norm: batch stats, running averages, eval mode
- Layer norm ignores the batch, so transformers use it

**Say it: logits and softmax**

- Softmax turns logits into probabilities summing to one
- Temperature: low sharpens, high flattens
- Confidence needs calibration and evaluation

## Homework

- [ ] Run softmax at temperatures 0.5, 1 and 2
- [ ] Derive w.grad = -24 by hand, then verify
- [ ] Vary the lab's local derivative
- [ ] Write a one-minute batch versus layer norm answer
