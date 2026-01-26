# Task: Probability Mass

## Objective
Understand Randomness (Temperature).

## Setup
*   Context: \"The sky is\"
*   Model Logits: `{"blue": 5.0, "gray": 3.0, "green": 0.1}`.

## Task
1.  Apply Softmax with Temperature $T=1.0$.
    *   `blue` dominates.
2.  Apply Softmax with Temperature $T=0.1$.
    *   `blue` becomes nearly 100%. (Deterministic).
3.  Apply Softmax with Temperature $T=2.0$.
    *   Distribution flattens. `gray` gets a good chance. `green` gets a non-zero chance.

## Question
When should you use High Temperature?
*   Answer: Creative writing, brainstorming, poetry.
When should you use Low Temperature?
*   Answer: Coding, math, factual QA.
