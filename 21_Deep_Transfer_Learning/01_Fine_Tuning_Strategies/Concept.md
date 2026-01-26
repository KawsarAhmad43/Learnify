# Advanced Fine-Tuning Strategies

## 1. Beyond "Freeze and Train"
Simply freezing layer 1-50 and training 51 is crude. Deep Networks (like BERT or ResNet152) are complex hierarchies.
We need gentler ways to adapt them.

## 2. Gradual Unfreezing (Chain-Thaw)
Instead of unfreezing everything at once (which shocks the optimizer), we unfreeze gradually.
1.  Train Head (Epoch 1).
2.  Unfreeze Last Block + Head (Epoch 2).
3.  Unfreeze Last 2 Blocks + Head (Epoch 3).
...
This allows the "high-level" features to adapt first before we touch the delicate "low-level" foundations.

## 3. Discriminative Fine-Tuning
Different layers capture different types of information.
*   **LR for Layer 1**: $1e-5$ (Base features like edges change very slowly).
*   **LR for Layer 100**: $1e-3$ (Task features need to change fast).
*   **Equation**: $\eta^{l-1} = \eta^l / 2.6$ (ULMFiT Formula).
