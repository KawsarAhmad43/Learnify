# Task: Ground Truth Lag

## Objective
The delay problem.

## Setup
*   You run a Credit Card Fraud detection model.
*   Model predicts: \"Fraud\" or \"Legit\".
*   **Problem**: You don't know the *Actual Outcome* (Label) immediately. You only find out it was fraud 30 days later when the customer complains.

## Task
1.  How do you calculate Accuracy today? You can't.
2.  You must rely on **Proxy Metrics** (Input Drift, Output Distribution).
3.  If yesterday the model predicted \"Fraud\" 1% of the time, and today it predicts \"Fraud\" 50% of the time, SOMETHING IS WRONG, even if you don't have the labels yet.

## Question
What is 'Feedback Loop'?
*   Answer: Model predicts X -> User reacts to X -> New Data is generated. E.g., Police go where the Crime Prediction model tells them -> Fewer crimes detected elsewhere -> Model thinks other areas are safe -> Loop.
