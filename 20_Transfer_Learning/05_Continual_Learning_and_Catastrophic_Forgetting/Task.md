# Task: Weight Drift

## Objective
Calculate L2 Drift.

## Setup
*   $W_{old} = [0.5, -0.5]$
*   $W_{new} = [0.6, -0.1]$

## Task
1.  Calculate L2 distance $\sqrt{\sum (w_{new} - w_{old})^2}$.
2.  Identify which weight changed the most.
    *   $|0.6 - 0.5| = 0.1$
    *   $|-0.1 - (-0.5)| = 0.4$ (This one drifted heavily).

## Question
If we know that Weight 2 is critical for the old task, is this drift acceptable? (No, it likely broke the old task).
