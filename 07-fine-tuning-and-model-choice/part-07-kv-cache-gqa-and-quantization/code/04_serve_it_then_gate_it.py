"""Zero to AI Engineer · Fine-tuning and Model Choice · Part 7 of 10
Slide: Serve it, then gate it
Run: python 04_serve_it_then_gate_it.py
"""
# serve a pre-quantised AWQ checkpoint
# (flag names depend on vLLM version)
cmd = ('vllm serve org/model-AWQ'
       ' --quantization awq')
print(cmd)

# gate: same prompts, several runs each
for p in ['fp16', 'int8', 'int4']:
    print(p, '-> golden set, TTFT, TPOT')
