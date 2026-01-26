# SHAP (Shapley Additive exPlanations)

## 1. Game Theory
Lloyd Shapley (Nobel Prize) solved a problem:
*   Three players (A, B, C) cooperate to earn $100.
*   A alone earns $10.
*   A + B earns $60.
*   A + B + C earns $100.
*   **Question**: How much of the $100 should each player get?

## 2. Shapley Value
It calculates the "Marginal Contribution" of a player across all possible coalitions.
*   Does adding A to B help?
*   Does adding A to C help?
*   Does adding A to (B+C) help?
*   Average these contributions.

## 3. SHAP in AI
*   **Players** = Features (Age, Income, Debt).
*   **Payout** = Prediction (Risk Score).
*   **SHAP Value**: How much the feature "Age=30" pushes the prediction away from the global average.
*   **Properties**:
    *   **Additivity**: Sum(SHAP Values) + Base Rate = Prediction.
    *   **Consistency**: If a model changes so that a feature is *more* important, its SHAP value must increase. (LIME fails this).
