# Task: Calculator vs Hallucination

## Objective
Accuracy check.

## Question
What is $34958 \times 29384$?
*   LLM (Direct): \"1,027,332,112\" (Likely wrong last digits).
*   Agent: `calculate(34958 * 29384)`.
    *   Python Tool runs: `1027206872`.
    *   Agent outputs: \"1,027,206,872\".

## Task
1.  Recognize the limit of Neural Networks (Approximate Function Approximators).
2.  Delegation is key.
3.  Why force a Biology Professor (LLM) to do arithmetic in their head when they can use a calculator?

## Conclusion
The smartest Agent is the one that knows what it DOESN'T know.
