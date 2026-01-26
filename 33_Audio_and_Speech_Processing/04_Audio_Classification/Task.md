# Task: Audio Transformers

## Objective
Beyond CNNs.

## Setup
*   CNNs are great, but they are \"Local\" (Convolution kernel looks at 3x3 pixels).
*   **Audio Spectrogram Transformer (AST)**:
    *   Slices the spectrogram into 16x16 patches.
    *   Flattens them into sequences.
    *   Feeds them to a Vision Transformer (ViT).
*   **Result**: SOTA on AudioSet (the ImageNet of Audio).

## Task
1.  **HuggingFace**: Use `transformers.ASTForAudioClassification`.
2.  **Fine-Tuning**: Download a pretrained AST and fine-tune it on your \"Dog vs Cat\" dataset.
3.  **Result**: Much higher accuracy than a custom CNN, because AST was pre-trained on millions of YouTube videos.

## Question
What is 'Source Separation'?
*   Answer: The "Cocktail Party Problem". Input: Recording of 2 people talking at once. Output: 2 separate audio files. (Conv-TasNet).
