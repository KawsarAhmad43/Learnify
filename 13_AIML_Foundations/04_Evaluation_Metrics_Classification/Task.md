# Task: Classification Metrics

## Task 1: Manual Calculation
Given these counts:
*   TP = 50
*   TN = 800
*   FP = 100
*   FN = 50
Calculate (on paper or mentally, then verify with code):
1.  Accuracy
2.  Precision
3.  Recall
4.  F1 Score

## Task 2: The Threshold Trade-off
Probabilities allow us to change the threshold (default 0.5).
1.  Use the `y_probs` from the Implementation notebook.
2.  If you set the threshold to **0.1** (predict 'Sick' if prob > 0.1), what happens to Recall? What happens to Precision?
3.  If you set the threshold to **0.9**, what happens?

## Task 3: Multiclass
Use `sklearn.metrics.classification_report` on a 3-class problem (0, 1, 2).
1.  Generate random `y_true` and `y_pred` with values 0, 1, 2.
2.  Print the full classification report.
