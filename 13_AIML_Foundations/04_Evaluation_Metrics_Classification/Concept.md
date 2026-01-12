# Evaluation Metrics: Classification

Comparing model accuracy is not enough. We need nuanced metrics.

## 1. The Confusion Matrix
For a Binary Classifier (Positive/Negative):
*   **True Positive (TP)**: Predicted Yes, Actual Yes.
*   **True Negative (TN)**: Predicted No, Actual No.
*   **False Positive (FP)**: Predicted Yes, Actual No (Type I Error). "False Alarm".
*   **False Negative (FN)**: Predicted No, Actual Yes (Type II Error). "Missed Discovery".

## 2. Core Metrics
*   **Accuracy**: $(TP+TN) / Total$. Good only if classes are balanced.
*   **Precision (P)**: $TP / (TP + FP)$. "Of all predicted positives, how many were right?" Important for Spam detection (don't delete real emails).
*   **Recall (R)**: $TP / (TP + FN)$. "Of all actual positives, how many did we find?" Important for Cancer detection (don't miss a case).
*   **F1 Score**: Harmonic mean of P and R. $2 * (P*R)/(P+R)$.

## 3. ROC and AUC
*   **ROC Curve**: Plots TPR (Recall) vs FPR (False Positive Rate) at various thresholds.
*   **AUC (Area Under Curve)**: Probability that the model ranks a random positive example higher than a random negative one. 1.0 is perfect, 0.5 is random guessing.
