# Research Project: Deep Transfer Learning (Fine-Tuning BERT)

## 1. Problem Understanding
*   **Context**: Specialized NLP. Using BERT (Google 2018) which knows general English, and teaching it "Medical English" or "Legal English".
*   **The Problem**: **Catastrophic Forgetting**. If you train BERT too hard on the new data, it forgets how to read basic English.
*   **Solution**: **Differential Learning Rates** and **Warmup Steps**.

## 2. Research Strategy
*   **Model**: **DistilBERT-Base-Uncased**. Faster/Lighter than BERT.
*   **Task**: Sentiment Analysis (Positive/Negative).
*   **Technique #1 (Freezing)**: First, freeze all BERT layers and train only the Classifier head for 1 epoch.
*   **Technique #2 (Unfreezing)**: Then, unfreeze BERT but use a very small learning rate (2e-5) to nudges the weights gently.
*   **Scheduler**: **Linear Warmup**. Start LR at 0, slowly ramp up, then decay. This prevents the gradients from exploding at the start.

## 3. Step-by-Step Plan
1.  **Dataset**: HuggingFace `imdb` (or mock equivalent).
2.  **Tokenization**: Pad to max length 512.
3.  **Training**: Use HuggingFace `Trainer`. Define `TrainingArguments` with `warmup_steps=500` and `weight_decay=0.01`.
4.  **Diagnostics**: Plot the Loss Curve. If it goes down, we are learning. If it goes up, we are "forgetting".
5.  **Inference**: Pipeline usage.
