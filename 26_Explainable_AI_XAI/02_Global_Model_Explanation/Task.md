# Task: Correlated Features

## Objective
The trap of permutation.

## Setup
*   Features: `Square_Feet` and `Number_of_Rooms`.
*   These are highly correlated (Big houses have more rooms).

## Task
1.  Permute `Square_Feet`.
2.  The model can still guess the price using `Number_of_Rooms`.
3.  Accuracy doesn't drop much.
4.  Permutation Importance says: \"Square Feet is not important\".
5.  Permute `Number_of_Rooms`.
6.  The model uses `Square_Feet`. Accuracy doesn't drop much.
7.  Conclusion: \"Rooms are not important\".

## Question
Both are important, but the method says neither is. Why?
*   Answer: Information redundancy. Permutation Importance UNDER-estimates importance when features are correlated. You need to group them or use SHAP.
