# Task: Memory Bandwidth

## Objective
The real bottleneck.

## Concept
LLM speed is memory-bound, not compute-bound.
Speed (Tokens/s) = Bandwidth (GB/s) / Model Size (GB).

## Task
1.  Hardware: RTX 4090.
    *   Bandwidth: 1000 GB/s.
2.  Model: Llama-70B (INT4).
    *   Size: 35 GB.
3.  Calculate Max Speed:
    *   $1000 / 35 = 28.5$ Tokens per second.

## Question
Why can't we go faster by buying a faster compute core?
*   Answer: Because we spend 99% of time *waiting* for weights to arrive from VRAM. Compute happens instantly. The only way to go faster is **Smaller Models** (Quantization) or **Faster VRAM** (HBM3).
