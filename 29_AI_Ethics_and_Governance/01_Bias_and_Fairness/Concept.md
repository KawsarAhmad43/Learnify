# Bias and Fairness

## 1. Types of Bias
*   **Historical Bias**: The world was biased, so the data is biased. (e.g., Doctors were mostly men in the 1950s. AI learns "Doctor = Man").
*   **Representation Bias**: The dataset under-represents a minority group. (e.g., Training Face Recognition only on light skin).
*   **Measurement Bias**: The input features are proxies. (e.g., Using "Arrest Rate" as a proxy for "Crime Rate". Arrests are influenced by policing policy).

## 2. Fairness Metrics
*   **Demographic Parity**: The acceptance rate must be equal for all groups. $P(\hat{Y}=1 | A=0) = P(\hat{Y}=1 | A=1)$.
*   **Equalized Odds**: The True Positive Rate must be equal for all groups. (It's okay to accept more Group A if Group A is actually more qualified, but you shouldn't make more *mistakes* on Group B).

## 3. Impossibility Theorem
You cannot satisfy all fairness metrics simultaneously.
If Group A has a higher base qualification rate than Group B:
*   Demographic Parity forces you to reject qualified Group A individuals.
*   Equal/Calibrated Accuracy allows disparate impact.
*   **Choice**: Society (Policy) must choose the metric, not the Data Scientist.
