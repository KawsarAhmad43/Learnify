# Task: ML Paradigms

## Task 1: Identify the Paradigm
For each scenario below, declare whether it is Supervised, Unsupervised, or Reinforcement Learning.
1.  Detecting fraudulent credit card transactions using a dataset of past transactions labeled "Fraud" or "clean".
2.  Grouping news articles into topics (Sports, Politics, etc.) without pre-existing labels.
3.  Teaching a robotic arm to stack boxes by giving it +1 point for a stack and -1 for a fall.
4.  Predicting tomorrow's stock price based on the last 10 years of data.

## Task 2: Notation Translation
Translate the following python code into our standard mathematical notation.
```python
# python code
X = [[1, 2], [3, 4]]
theta = [0.5, 0.5]
y_pred = X[0][0]*theta[0] + X[0][1]*theta[1]
```
*   What is $m$?
*   What is $n$?
*   Write the equation for $y_{pred}$ using vector notation (e.g., $\theta^T x$).

## Task 3: The Design Matrix
Create a NumPy array representing the Design Matrix $X$ for this dataset:

| House Size ($feet^2$) | # Bedrooms | Price ($) |
| --------------------- | ---------- | --------- |
| 2104                  | 3          | 400k      |
| 1600                  | 3          | 330k      |
| 2400                  | 3          | 369k      |
| 1416                  | 2          | 232k      |

*   Hint: Price is $y$, not part of $X$.
*   Print the shape of $X$.
