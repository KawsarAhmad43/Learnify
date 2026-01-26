# CI/CD for Machine Learning

## 1. CI (Continuous Integration)
*   User pushes code to GitHub.
*   **Trigger**: A script runs automatically.
*   **Action**: Linting (Black/Flake8), Unit Tests (Pytest).
*   **ML Specific**: Check if `model.predict()` still outputs the correct shape.

## 2. CD (Continuous Delivery/Deployment)
*   If Tests Pass -> Deploy.
*   **CT (Continuous Training)**: Retrain the model on new data, evaluate it, and if `metrics > threshold`, push to production.

## 3. CML (Continuous Machine Learning)
A tool that allows GitHub Actions to generate reports.
*   The script trains a model and plots a Confusion Matrix.
*   The script posts that image as a comment on your Pull Request.
*   **Benefit**: You see the model performance *before* you merge the code.
