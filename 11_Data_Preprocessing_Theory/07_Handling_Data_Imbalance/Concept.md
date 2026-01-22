# Handling Data Imbalance

## 1. The Real-Life Problem
In many real-world scenarios, the "positive" class (what we want to find) is extremely rare.
*   **Fraud Detection**: 99.9% legit, 0.1% fraud.
*   **Disease Diagnosis**: 95% healthy, 5% sick.
*   **Manufacturing Defects**: 99% good, 1% defective.

## 2. The Accuracy Paradox
If you build a model on 99% legit data, the model can achieve **99% accuracy** by simply predicting "Legit" for everything.
*   **Result**: It misses EVERY fraud case. The model is useless despite high accuracy.
*   **Metric**: We must use **Precision**, **Recall**, **F1-Score**, or **ROC-AUC** instead of Accuracy.

## 3. Strategies

### Resampling
Change the training data to be more balanced.
*   **Undersampling**: Randomly remove majority samples. Good for big data, but loses information.
*   **Oversampling**: Duplicate minority samples. Can lead to overfitting.
*   **SMOTE (Synthetic Minority Over-sampling Technique)**: Instead of duplicates, it generates *new* synthetic samples by interpolating between existing minority samples.

### Algorithmic (Class Weights)
Keep the data as is, but tell the model to pay more attention to the minority class.
*   **Cost-Sensitive Learning**: Penalize the model 10x or 100x more for misclassifying the minority class.
*   In scikit-learn: `class_weight='balanced'`.

## 4. Anomaly Detection
If the minority class is truly rare (e.g., 1 in a million), treat it as an Outlier Detection problem (One-Class SVM, Isolation Forest) rather than a classification problem.
