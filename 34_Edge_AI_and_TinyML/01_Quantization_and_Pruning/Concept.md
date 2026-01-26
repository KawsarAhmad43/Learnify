# Quantization and Pruning

## 1. The Cost of Float32
*   Standard Deep Learning uses 32-bit Floating Point numbers (e.g., 3.14159...).
*   **Memory**: 4 bytes per weight. ResNet-50 has 25M params -> 100MB.
*   **Compute**: Float multiplication is expensive in silicon.

## 2. Quantization (Int8)
*   Convert weights to 8-bit Integers [-128, 127].
*   **Memory**: 1 byte per weight. ResNet-50 -> 25MB. (4x smaller).
*   **Compute**: Integer math is blazing fast and energy efficient.
*   **Accuracy Drop**: Usually < 1% if done correctly (Post-Training Quantization).

## 3. Pruning
*   Many neurons don't do anything useful.
*   **Magnitude Pruning**: If a weight is very small (0.0001), set it to exactly 0.
*   **Sparse Format**: Store only the non-zero weights.
*   **Result**: 90% of connections can often be removed with no loss in accuracy.
