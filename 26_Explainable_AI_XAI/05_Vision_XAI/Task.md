# Task: Adversarial Attacks

## Objective
Fragility.

## Setup
*   Image of a Panda.
*   Add tiny, invisible noise (Adversarial Patch).
*   Model predicts: \"Gibbon\" (99% confidence).

## Task
1.  Run Grad-CAM on the adversarial image.
2.  Result: The heatmap focuses intently on the *invisible noise pattern*, not the Panda's face.
3.  This proves the model is broken, even if the human eye can't see why.

## Question
Can XAI detect deepfakes?
*   Answer: Yes. Often deepfakes have subtle artifacts (e.g., irregular blinking) that XAI heatmaps will latch onto as "unnatural".
