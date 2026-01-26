# Task: The Forget Gate

## Objective
Understand how the Forget Gate works.

## Formula
$f_t = \sigma(W_f \cdot [h_{t-1}, x_t] + b_f)$
Keep it simple: Assume $f_t$ is a manual switch.

## Task
1.  Assume Cell State $C_{t-1} = 100$ (Strong memory of \"Subject is Plural\").
2.  New input $x_t$ indicates a full stop \".\".
3.  The Forget Gate $f_t$ should trigger to clear the memory for the next sentence.
    *   Set $f_t = 0.1$.
4.  Calculate new $C_t = C_{t-1} \times f_t$.

## Question
What happens if $f_t$ stays at $1.0$? (The memory leaks into the next sentence, confusing the grammar).

Write a script to simulate a memory value decaying over 5 steps with $f_t = 0.5$.
