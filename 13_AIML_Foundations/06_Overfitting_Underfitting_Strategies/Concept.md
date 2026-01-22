# Overfitting & Underfitting: The Diagnostic Playbook

## 1. Scenario: Medical Diagnosis (Cancer Risk)
Imagine classifying patients as "High Risk" or "Low Risk" based on Age and Biomarker Levels.
*   **Goal**: Generalize to *new* patients. We don't care if we memorize the 500 patients in the database if we kill the next patient by misdiagnosing them.

## 2. The Diagnostic Matrix
How to know what's wrong with your model? Look at the Training and Testing errors.

| Train Error | Test Error | Diagnosis | Meaning |
| :--- | :--- | :--- | :--- |
| **High** | **High** | **Underfitting** (High Bias) | The model is too "stupid". It can't even learn the training data. |
| **Low** | **High** | **Overfitting** (High Variance) | The model is a "memorizer". It learned the noise, not the signal. |
| **Low** | **Low** | **Success** | The model generalizes well. |
| **High** | **Low** | **Data Leakage / Fluke** | Check your code. You likely tested on training data or have a bug. |

## 3. The Playbook: How to Fix It

### Situation A: Underfitting (Train Poor, Test Poor)
*   **The Fix**: **Increase Complexity**.
*   **Actions**:
    1.  Switch algorithms (Linear -> Random Forest / Neural Net).
    2.  Add more features (Polynomials, Interactions).
    3.  Decrease Regularization (Reduce Lambda/Alpha).
    4.  Train longer (more epochs).

### Situation B: Overfitting (Train Great, Test Poor)
*   **The Fix**: **Reduce Complexity**.
*   **Actions**:
    1.  **More Data**: The absolute best cure. Hard to overfit data that represents the whole world.
    2.  **Regularization**: Add L1/L2 penalties.
    3.  **Simplify Model**: Reduce tree depth, reduce neuron count, reduce polynomial degree.
    4.  **Feature Selection**: Drop irrelevant noise columns.
