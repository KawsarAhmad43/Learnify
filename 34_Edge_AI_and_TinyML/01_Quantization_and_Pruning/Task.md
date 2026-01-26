# Task: Knowledge Distillation

## Objective
Teacher-Student Training.

## Setup
*   You have a giant ResNet-152 (Teacher) with 90% accuracy.
*   You need a tiny MobileNet (Student) for a phone.
*   Training MobileNet from scratch gives 70%.

## Task
1.  **Distillation**: Train the Student to mimic the *Logits* (Softmax output) of the Teacher, not just the hard labels.
2.  **Why?**: The Teacher says "This looks 90% like a Dog, 9% like a Cat, 1 like a Car".
3.  The "9% Cat" is valuable information (Dark Knowledge). It tells the Student that Dogs look like Cats.
4.  **Result**: Student gets 80% accuracy.

## Question
What is 'Quantization Aware Training' (QAT)?
*   Answer: Simulating quantization *during* training. The model learns to round its weights to integers while computing gradients. This yields higher accuracy than Post-Training Quantization (PTQ).
