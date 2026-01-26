# Adapters and LoRA

## 1. The Fine-Tuning Problem
GPT-3 has 175 Billion parameters.
Finetuning ALL of them for 1 specific task (e.g., Chess Commentary) is expensive:
1.  **Storage**: A checkpoint is 350GB. If you have 10 tasks, you need 3.5TB.
2.  **Memory**: Updating gradients for 175B parameters requires impossible amounts of VRAM.

## 2. Parameter Efficient Fine Tuning (PEFT)
Don't touch the original weights ($W$).
Add a tiny module ($\Delta W$) that learns the changes.
Output = $W(x) + \Delta W(x)$.

## 3. LoRA (Low-Rank Adaptation)
Hypothesis: The change needed to adapt a model is "Low Rank" (simple).
*   Instead of a full $1000 \times 1000$ matrix update (1M params).
*   We use two small matrices: $A$ ($1000 \times 8$) and $B$ ($8 \times 1000$).
*   $A \times B$ creates a $1000 \times 1000$ update.
*   Parameters: $8000 + 8000 = 16,000$.
*   **Savings**: $16k$ vs $1M$ (98% reduction).
