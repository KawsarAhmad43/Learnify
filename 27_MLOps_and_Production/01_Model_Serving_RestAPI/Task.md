# Task: Throughput Calculation

## Objective
Capacity Planning.

## Setup
*   Model Inference Time: 100ms (0.1s).
*   Single Threaded Server (Flask).
*   Requests per second: 1 / 0.1 = 10 RPS.

## Task
1.  We need to handle 1000 RPS.
2.  How many workers/servers do we need?
3.  Simple Math: $1000 / 10 = 100$ workers.
4.  **Optimization**: If we Batch requests (process 32 at once), inference might take 150ms total.
    *   Throughput = $32 / 0.15 = 213$ RPS/worker.
    *   Now we only need 5 servers.

## Question
Why is GPU serving hard?
*   Answer: GPUs are expensive. You can't just spin up 100 GPUs like you can with CPUs. You must batch aggressively to saturate the GPU.
