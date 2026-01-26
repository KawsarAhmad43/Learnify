# Task: Simpson's Reversal

## Objective
Detecting hidden bias.

## Setup
*   Model approval rate: 60% for Men, 60% for Women.
*   Slice by Department:
    *   Engineering: Men (80% approved), Women (90% approved).
    *   HR: Men (10% approved), Women (20% approved).
    *   Wait... Women are approved *higher* in BOTH departments, but *same* overall? How?
*   Reason: Most women applied to HR (Low approval rate in general). Most men applied to Engineering (High approval rate).

## Task
1.  This is a classic paradox.
2.  If you only look at the Global Average, you miss the story.
3.  Slice Analysis is mandatory for fairness.

## Question
What is a 'OOD' error in error analysis?
*   Answer: Out of Distribution. The model fails because the input (Snow) looks nothing like the training data (Desert). XAI helps identify these clusters.
