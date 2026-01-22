# Supervised ML Model Pipeline

## 1. Scenario: Credit Risk Assessment
A bank needs to predict Loan Defaults.
*   **The Challenge**: We don't know which mathematical approach matches the chaotic reality of human financial behavior. Is it linear? Is it rule-based? Is it distance-based?

## 2. Why check ALL algorithms? (No Free Lunch Theorem)
No single algorithm is best for every problem.
*   **Logistic Regression**: Best if the relationship is simple/linear. Fast, Interpretable.
*   **KNN**: Best if similar people behave similarly. (Needs scaling).
*   **SVM**: Best for high-dimensional complex boundaries. (Slow on large data).
*   **Decision Trees**: Best if there are clear "If-Then" cutoffs.
*   **Random Forest / XGBoost**: Best for messy, non-linear, interacting data. Usually the accuracy winners.
*   **Naive Bayes**: Best for text/counts (independent features).

## 3. The "Grand Pipeline"
We use `GridSearchCV` to try them all.
*   *Note*: Some algorithms (SVM, KNN, Logistic) **require** Scaling. Trees (RF, XGB) don't care, but it doesn't hurt them. So we usually scale everything in the pipeline to be safe.

## 4. Can we mix Regression and Classification?
**Yes!** It's called **Stacking** or **Cascading**.
*   **Scenario (Real Estate Flip)**:
    1.  **Step 1 (Regression)**: Predict the *Potential Sale Price* of a house.
    2.  **Step 2 (Classification)**: Use that predicted price (along with other features) to predict *Will this flip be Profitable?* (Yes/No).
*   **In a Pipeline**: You define Model 1. You take its output (`y_pred`). You feed that as an input feature (`X_new`) into Model 2.
