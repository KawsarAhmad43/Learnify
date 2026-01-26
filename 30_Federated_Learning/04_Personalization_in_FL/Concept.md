# Personalization in FL

## 1. Global vs Local
*   **Global Model**: \"Average\" intelligence. Good at everything, great at nothing.
*   **Local Model**: Specialized to YOU.
*   **Goal**: We want the best of both worlds.

## 2. Meta-Learning (MAML)
"Learning to Learn".
*   Instead of learning a model that is accurate immediately...
*   We learn a model that can *become* accurate with just 1 gradient step on your data.
*   **Application**: The Global Model is a \"Good Initialization\". When it lands on your phone, your phone runs 5 epochs of Fine-Tuning on your text messages. Now it speaks like you.

## 3. Multi-Task Learning
Treat each user as a separate \"Task\".
*   The model has a shared \"Backbone\" (Feature Extractor) that is aggregated globally.
*   The model has a private \"Head\" (Classifier) that stays local and is never shared.
