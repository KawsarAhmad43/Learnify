# Counterfactual Explanations

## 1. The Human Way
Humans don't think in gradients. We think in "What Ifs".
*   "If I hadn't eaten that sushi, I wouldn't be sick."
*   "If I had earned $5k more, I would have got the loan."

## 2. DiCE (Diverse Counterfactual Explanations)
A framework that finds the **Minimal Change** needed to flip the prediction.
*   **Original**: {Income: 40k, Credit Score: 600} -> Denied.
*   **Use Gradient Descent**: To find a point $x'$ such that $f(x') = Approved$ and $|x - x'|$ is minimized.
*   **Result**: {Income: 45k, Credit Score: 600} -> Approved.

## 3. Actionability
A good counterfactual must be **Actionable**.
*   Bad: "If you were 10 years younger, you would be approved." (User cannot change Age).
*   Good: "If you pay off $2k debt, you would be approved." (User can do this).
