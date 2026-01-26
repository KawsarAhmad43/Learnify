# Task: Silent Failures

## Objective
Detecting bad models that don't crash.

## Setup
*   Your pipeline checks `assert accuracy > 0.80`.
*   New model training: Accuracy = 0.85. (Passes).
*   Deployment happens.
*   **Disaster**: The model predicts \"True\" for EVERYTHING. (Class imbalance: 85% of data is True).
*   The model learned to be lazy, and the CI test was too weak to catch it.

## Task
1.  Improve the test.
2.  Add a check for `Recall` and `Precision`, not just Accuracy.
3.  Add a `DummyClassifier` check (Does your model beat a model that just guesses the majority class?).

## Question
What is 'Shadow Mode'?
*   Answer: Running the new model in production alongside the old one, but NOT showing its results to the user. You just log its predictions to compare against the old (trusted) model. Safer than Canary.
