# Task: Catastrophic Forgetting

## Objective
Stability.

## Setup
*   Your Face ID model works great.
*   You grew a beard. It learned the beard.
*   You shaved the beard.
*   **Problem**: It forgot your face without a beard. It locked you out.
*   This is Catastrophic Forgetting. By learning new data (Beard), it overwrote old data (No Beard).

## Task
1.  **Replay Buffer**: Store a small set of old examples (encrypted) and mix them with new examples during training.
2.  **Elastic Weight Consolidation (EWC)**: Identify which weights are critical for "No Beard" and freeze them (make them elastic/hard to change), while allowing other weights to learn "Beard".

## Question
What is 'CoreML'?
*   Answer: Apple's framework. It is highly optimized for the Neural Engine (ANE). If you want your app to be fast on iPhone, you must convert TFLite/PyTorch to CoreML.
