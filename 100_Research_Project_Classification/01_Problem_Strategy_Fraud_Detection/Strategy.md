# Research Project: Credit Card Fraud Detection

## 1. Problem Understanding
*   **Context**: A bank wants to stop fraudulent transactions *before* they are processed.
*   **The Data**: The famous [Credit Card Fraud Detection](https://www.kaggle.com/mlg-ulb/creditcardfraud) dataset.
    *   **Imbalance**: 284,315 legitimate transactions vs 492 frauds. (0.172% fraud).
    *   **Anonymity**: Features V1-V28 are PCA transformed (for privacy). 'Time' and 'Amount' are the only interpretable features.
*   **The Trap**: If you train a model to just say "Not Fraud", it achieves 99.8% accuracy. But it captures 0 frauds. This is a business disaster.

## 2. Research Strategy
*   **Metric Selection**:
    *   **Precision**: "When we say it's fraud, is it?" (We don't want to block legit users too often).
    *   **Recall (Sensitivity)**: "Did we catch all the frauds?" (We cannot afford to miss fraud).
    *   **AUPRC (Area Under Precision-Recall Curve)**: The gold standard for imbalanced data. (Better than ROC-AUC here).

*   **Handling Imbalance**:
    1.  **Class Weights**: Tell the model that "1 Error on Fraud class is equal to 100 Errors on Normal class".
    2.  **SMOTE (Synthetic Minority Over-sampling Technique)**: Generate fake "Fraud" examples to balance the dataset.
    3.  **Undersampling**: Throw away some legit data (RISKY - loss of information).

## 3. Step-by-Step Plan
1.  **EDA**: Vizualize the distribution. Confirm the massive imbalance. Check if 'Amount' differs for fraud (spoiler: Frauds are often small amounts to test the card, or massive amounts to drain it).
2.  **Preprocessing**: Scale 'Amount' and 'Time'.
3.  **Baseline**: Logistic Regression with `class_weight='balanced'`.
4.  **Advanced Model**: Random Forest or XGBoost.
5.  **Oversampling**: Apply SMOTE only to the *Training Set*. Never touch the Test Set (Data Leakage).
6.  **Evaluation**: Plot Confusion Matrix and PR Curve.
