# Task: Compression Ratio

## Objective
Calculate storage savings.

## Base Model
*   70 Billion Parameters.
*   Float16 (2 bytes per param).
*   Size = $70 \times 2 = 140$ GB.

## Optimized Model
*   Distilled to 7 Billion Parameters.
*   Quantized to Int4 (0.5 bytes per param).

## Task
1.  Calculate size of Optimized Model.
    *   $7 \times 0.5$ GB.
2.  Calculate ratio.

## Question
Can the optimized model fit on a standard 16GB laptop RAM? (Yes/No).
*   Answer: Yes, easily (3.5GB < 16GB). The original model required 4x A100 GPUs.
