# Task: Dimensions vs Speed

## Objective
Trade-offs.

## Setup
*   OpenAI Embedding: 1536 dimensions.
*   Database: 1 Million Vectors.
*   Size: $1,000,000 \times 1536 \times 4$ bytes (FP32).

## Task
1.  Calculate RAM Usage.
    *   $6.144 \times 10^9$ bytes $\approx 6$ GB RAM.
    *   This fits in memory easily.
2.  If we scale to 1 Billion Vectors?
    *   6 TB RAM. (Expensive!).

## Question
How do we store 1 Billion vectors cheaply?
*   Answer: **Product Quantization (PQ)**. Compress the vector from floats to short codes. Or **DiskANN** (Keep the index on SSD, not RAM).
