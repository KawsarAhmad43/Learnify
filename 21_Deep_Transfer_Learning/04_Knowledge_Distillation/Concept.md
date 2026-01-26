# Knowledge Distillation

## 1. Teacher and Student
*   **Teacher**: A huge, powerful model (e.g., Llama 70B, ResNet152). High accuracy, slow.
*   **Student**: A tiny, fast model (e.g., Llama 1B, MobileNet). Low accuracy, fast.

## 2. Hard Labels vs Soft Labels
*   **Hard Label**: "This is a Dog." (One-Hot: [0, 1, 0]).
*   **Soft Label** (Teacher Output): "This is mostly a Dog (0.9), but it looks a bit like a Wolf (0.09) and not at all like a Car (0.001)."
*   **The Magic**: The *Student* learns more from the 0.09 Wolf probability (The "Dark Knowledge") than from the hard label. It learns *relationships* between classes.

## 3. Loss Function
$L_{total} = (1 - \alpha) L_{CE}(Student, HardLabel) + \alpha L_{KL}(Student, Teacher)$
*   $L_{CE}$: Don't be wrong.
*   $L_{KL}$: Imitate the Teacher's nuances.

## 4. Temperature ($T$)
We soften the distributions by dividing logits by $T > 1$ before Softmax. High $T$ reveals even more hidden relationships.
