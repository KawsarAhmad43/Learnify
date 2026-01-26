# Model Monitoring and Drift

## 1. Code Doesn't Rot, Data Does
*   Traditional Software: If it works today, it works tomorrow (unless dependencies change).
*   ML Software: Even if code is untouched, accuracy degrades because the **World Changes**.

## 2. Types of Drift
1.  **Data Drift** (Covariate Shift): The inputs ($X$) change. (e.g., Users start uploading 4K images instead of 1080p).
2.  **Concept Drift**: The relationship ($X \rightarrow Y$) changes. (e.g., "Spam" emails evolve new tricks. The same email text that was safe yesterday is spam today).

## 3. Detecting Drift
*   **Statistical Tests**: Compare the distribution of Training Data vs Production Data (Last 24 hours).
*   **KS Test (Kolmogorov-Smirnov)**: Are these two histograms different?
*   **PSI (Population Stability Index)**: Measure of shift.

## 4. Remediation
*   Alert the team.
*   **Retrain**: Use the new data to update the model weights.
