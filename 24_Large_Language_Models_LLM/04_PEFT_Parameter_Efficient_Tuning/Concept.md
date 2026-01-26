# PEFT (Parameter Efficient Fine Tuning)

## 1. The Problem: Full Finetuning is Impossible
To finetune Llama-70B:
*   Params: 70 Billion.
*   Optimizer States (Adam produces 2 states per param): 140 Billion floats.
*   Gradients: 70 Billion floats.
*   **VRAM Needed**: > 600 GB A100s. (Cost: Thousands of dollars).

## 2. LoRA (Low-Rank Adaptation)
Hypothesis: We don't need to update ALL weights. The "change" in weights ($\Delta W$) has a low rank.
*   $W_{new} = W_{old} + \Delta W$.
*   Instead of storing $\Delta W$ ($d \times d$ matrix), store $A \times B$.
    *   $A$: $d \times r$.
    *   $B$: $r \times d$.
    *   $r$: Rank (e.g., 8 or 16).
*   **Memory Savings**: $10,000 \times 10,000$ matrix (100M params) becomes two $10,000 \times 8$ matrices (0.16M params). **99.9% Reduction**.

## 3. QLoRA
Quantize the base model ($W_{old}$) to 4-bit to save VRAM, then attach LoRA adapters in 16-bit.
Result: Finetune a 70B model on a single 48GB GPU.
