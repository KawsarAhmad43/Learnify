# Global Model Explanation

## 1. Feature Importance
Question: "Overall, what matters most to this model?"
*   Is it Price? Location? Size?

## 2. Permutation Importance (Model Agnostic)
How do we test importance without knowing the math inside?
*   **Method**:
    1.  Measure baseline accuracy (e.g., 90%).
    2.  Take the "Age" column and shuffle it randomly (destroying its information).
    3.  Measure accuracy again (e.g., 88%).
    4.  Importance = $90 - 88 = 2\%$.
    5.  Now shuffle "Income". Accuracy drops to 60%.
    6.  Importance = $30\%$.
*   **Conclusion**: Income is critical. Age is minor.

## 3. Partial Dependence Plots (PDP)
Question: "How does Price change as Size increases, holding everything else constant?"
*   Plot $x=Size$, $y=Prediction$.
*   Usually shows a monotonic increase, then a plateau.
