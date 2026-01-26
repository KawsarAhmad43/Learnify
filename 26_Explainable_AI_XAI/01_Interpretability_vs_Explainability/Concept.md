# Interpretability vs Explainability

## 1. Intrinsic Interpretability (Transparent Models)
*   **Linear Regression**: $Price = 100 \times Size + 50 \times Rooms$. We know EXACTLY how it works. A 1-unit increase in Size adds 100 to Price.
*   **Decision Tree**: `If age > 50 and smoker = True -> Risk`. We can trace the path.
*   **Limitation**: These models are usually too simple for complex tasks (like Image Recognition).

## 2. Explainability (Post-Hoc on Black Boxes)
*   **Neural Network**: Input -> [Processing by 1 Billion numbers] -> "Cat".
*   We cannot understand the 1 Billion numbers.
*   **Post-Hoc Explanation**: We try to reverse-engineer WHY it said "Cat", usually by approximating the Black Box with a simpler White Box (like LIME).

## 3. The Trade-off
*   **Accuracy vs Explainability**: Generally, more complex models (Deep Learning) are more accurate but less explainable.
*   **Goal of XAI**: Get High Accuracy AND Trust.
