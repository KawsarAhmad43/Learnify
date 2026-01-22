# Pipelines and Best Practices

## 1. The Preprocessing Sequence
Data flow in production ML should be linear and automated.
**Sequence**:
1.  **Split** data into Train and Test sets.
2.  **Impute** missing values (fit on Train, transform on Test).
3.  **Encode** categorical variables.
4.  **Scale** numerical variables.
5.  **Engineer** new features.
6.  **Train** the model.

## 2. Scikit-Learn Pipeline
A `Pipeline` chains transformers and an estimator together.
*   **Benefits**:
    *   **Automation**: Calling `fit()` on the pipeline fits all steps sequentially.
    *   **Safety**: Automatically applies transformations to validation/test data without leaking information.

## 3. Data Leakage
Leakage occurs when info from the test set (or future) "leaks" into the training process.
*   **Common Mistake**: Scaling the *entire* dataset before splitting. The mean used for scaling contains information about the test set!
*   **Fix**: Split FIRST. Fit scaler ONLY on training data. Transform both.

## 4. ColumnTransformer
Allows applying different preprocessing steps to different columns (e.g., OneHotEncode 'City' but Scale 'Age').
