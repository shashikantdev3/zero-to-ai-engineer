# Fine-tuning and Model Choice · Part 10 of 10: Running Models Locally and at Scale

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Local inference: GGUF, llama.cpp and Ollama
2. Serving engines: vLLM, TGI, SGLang and TensorRT-LLM
3. Running vLLM's OpenAI-compatible server
4. Replicas and autoscaling

## Key takeaways

- GGUF and Ollama: local and offline, not crowds
- Engines: benchmark on your own traffic
- Three flags are your admission control
- Replicas for throughput; scale on queue depth

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_pull_run_point_at_localhost.py` | Pull, run, point at localhost | yes |
| `code/02_the_serve_command_part_by_part.py` | The serve command, part by part | yes |
| `code/03_calling_the_compatible_endpoint.py` | Calling the compatible endpoint | yes |
| `code/04_lab_size_a_replica_fleet.py` | Size a replica fleet | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/04_lab_size_a_replica_fleet.py` prints:

```text
Peak concurrency: 200
Per replica: 40
Replicas: 5 + 1 warm spare
Scale out: True
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. A team plans to serve thousands of users with Ollama. Good idea?**

- A. Yes, if the model is quantised to Q4
- B. No, use a serving engine like vLLM
- C. Yes, it has an OpenAI-compatible API

<details><summary>Answer</summary>

**B. No, use a serving engine like vLLM**. Ollama is for local work, not thousands of users

</details>

**2. How should you choose a serving engine?**

- A. Benchmark each on your own traffic
- B. Pick whichever supports the most models
- C. Pick the top published benchmark

<details><summary>Answer</summary>

**A. Benchmark each on your own traffic**. Benchmarks depend on workload shape. Test yours.

</details>

**3. You set max model length to the model's full context window. What changes?**

- A. Fewer users can be served at once
- B. Answers get better for every request
- C. Nothing, unless long prompts arrive

<details><summary>Answer</summary>

**A. Fewer users can be served at once**. Bigger context cap, fewer concurrent sequences

</details>

**4. What should a GPU model server autoscale on?**

- A. The number of registered users
- B. CPU utilisation, like web services
- C. Queue depth or waiting requests

<details><summary>Answer</summary>

**C. Queue depth or waiting requests**. GPUs saturate at low CPU. Scale on the queue.

</details>

## Say it in the interview

**Local inference, in your words**

- GGUF via llama.cpp or Ollama for local work
- Many concurrent users: move to vLLM
- Evaluate the exact quantised file you ship

**Serving engines, in your words**

- Same problems: batching, KV memory, quantisation
- Default: vLLM, no app code changes
- SGLang for prefixes, TensorRT-LLM for NVIDIA

**Running vLLM, in your words**

- vllm serve plus three deliberate flags
- Lower the caps before buying GPUs
- Change the base URL, rerun the evals

**Scaling, in your words**

- Users to peak concurrency, with Little's law
- Peak over per-replica capacity, plus headroom
- Scale on queue, keep warm, TP only to fit

## Homework

- [ ] Check which engine Ollama uses for one model
- [ ] Confirm TGI's current status in its README
- [ ] Write vLLM's three flags and what each caps
- [ ] Rerun the lab with peak concurrency 300
