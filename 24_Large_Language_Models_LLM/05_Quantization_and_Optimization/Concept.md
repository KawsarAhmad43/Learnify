# Quantization and Optimization

## 1. Number Formats
*   **FP32 (Float32)**: 4 bytes. 7 decimals precision. Default for training.
*   **FP16/BF16**: 2 bytes. Sufficient for LLM training.
*   **INT8**: 1 byte. Good for Inference.
*   **FP4/INT4**: 0.5 bytes. The modern standard for running large models on laptops.
*   **1-bit (BitNet)**: Extreme research frontier (Weights are just -1 or 1).

## 2. Post-Training Quantization (PTQ)
Take a trained FP16 model and clamp weights to the nearest integer.
*   Outliers: Some weights are hugely important (100.5). Clamping them to 127 ruins the model.
*   **SmoothQuant**: Mathematically smooth out outliers so everything fits in INT8.

## 3. KV Cache
In inference, we generate one token at a time.
*   Token 1: `input=["The"], key_values=[K_1, V_1]`.
*   Token 2: `input=["cat"], key_values=[K_2, V_2]`.
*   We shouldn't re-compute K_1, V_1.
*   **Cache**: Store K/V of previous tokens in VRAM. This trades Memory for Speed.

## 4. Flash Attention
Standard Attention computes an $N \times N$ matrix. This is huge.
Flash Attention breaks the matrix into tiles that fit in GPU SRAM (L1 Cache), confusing Memory bandwidth bottlenecks.
Result: 3x-5x faster training.
