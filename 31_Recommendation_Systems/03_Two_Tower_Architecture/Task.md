# Task: Negative Sampling

## Objective
Training Data imbalance.

## Setup
*   Users only click on things they like.
*   Dataset: `(User1, MovieA, Click=1)`.
*   We have NO data for `Click=0`. (Implicit Feedback).
*   If we train only on `1s`, the model learns to output \"1\" for everything.

## Task
1.  **Uniform Negative Sampling**: For every positive sample, pick 5 random movies and label them `0`.
2.  **Hard Negative Sampling**: Pick movies that the user *almost* clicked (e.g., highly ranked by the model but not clicked). This improves learning.

## Question
What is 'In-Batch Negatives'?
*   Answer: Efficient training trick. If you have a batch of 64 `(User, Item)` pairs, you treat `(User_i, Item_j)` as a negative sample for all $i \neq j$. This gives you $64 \times 63$ negatives for free without reading extra data.
