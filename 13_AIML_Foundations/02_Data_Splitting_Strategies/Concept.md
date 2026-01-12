# Data Splitting Strategies

The Golden Rule of ML: **Never test on the data you trained on.**

## 1. Why Split?
If you evaluate your model on the same data used to update its parameters, you get a biased, optimistic score. This is like memorizing the answers to a test before taking it.

## 2. The Standard Splits
### A. The 2-Way Split (Simple)
*   **Training Set (80%)**: Used to learn the weights $\theta$.
*   **Test Set (20%)**: Held out until the very end to estimate real-world performance.

### B. The 3-Way Split (For Tuning)
If you need to tune hyperparameters (like learning rate, tree depth):
*   **Training Set (60-70%)**: Inner loop optimization.
*   **Validation Set (15-20%)**: Used to select the best model hyperparameters.
*   **Test Set (15-20%)**: Final check. **Never** use this to make decisions.

## 3. Cross-Validation (K-Fold)
When data is small, splitting "wastes" data. CV solves this.
1.  Split data into K folds (e.g., 5).
2.  Train on K-1 folds, validate on the remaining 1.
3.  Repeat K times, rotating the validation fold.
4.  Average the scores.

## 4. Data Leakage (The Enemy)
Leakage happens when information from the target (y) seeps into the training data (X) in a way that won't exist in production.
*   **Example**: Including "Future Data" (predicting rain today, but including "Did it rain?" boolean from tomorrow).
*   **Preprocessing Leakage**: Scaling/Normalizing the entire dataset *before* splitting. You must split *first*, then fit scaler on Train, then transform Test.
