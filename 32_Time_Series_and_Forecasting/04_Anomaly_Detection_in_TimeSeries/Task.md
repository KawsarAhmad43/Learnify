# Task: False Positives

## Objective
The Boy Who Cried Wolf.

## Setup
*   Your Anomaly Detector has 99% accuracy.
*   But anomalies only happen 0.01% of the time.
*   **Result**: You flood the operator with False Alarms. They turn off the system.

## Task
1.  **Metric**: Do NOT use Accuracy. Use **Precision** (If I say it's an anomaly, is it really?) and **Recall** (Did I catch all anomalies?).
2.  **Human in the Loop**: AI provides a \"Risk Score\". Human makes the final call. The AI learns from the Human's feedback (Active Learning).

## Question
What is 'Concept Drift' vs 'Anomaly'?
*   Answer:
    *   **Anomaly**: A temporary deviation (Spike).
    *   **Drift**: A permanent change in the baseline (Level Shift).
    *   If the vibration increases and STAYS high, is it drift or a broken engine? (Requires domain knowledge).
