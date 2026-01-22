# Decision Trees

## 1. Scenario: Loan Approval
A bank officer wants a checklist to approve loans.
*   **Rules**: 
    1.  Is Income > $50k? (No -> Deny)
    2.  If Yes, is Credit Score > 700? (Yes -> Approve, No -> Deny).
*   **Decision Tree**: Automates learning these "If-Then" rules.

## 2. Key Concepts
*   **Splitting**: How to divide the data?
*   **Entropy / Gini Impurity**: Metrics to measure "messiness". We want splits that result in pure leaves (e.g., a node with ONLY 'Approve' is pure).
    *   **Goal**: Maximize Information Gain (Reduction in Entropy).
*   **Pruning**: Cutting off branches to prevent Overfitting (Trees love to memorize noise).

## 3. Pros and Cons
*   **Pros**: Highly interpretable (you can draw the flowchart).
*   **Cons**: Prone to Overfitting, unstable (small change in data changes the whole tree).
