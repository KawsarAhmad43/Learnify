# Task: Voice Cloning

## Objective
Identity Transfer.

## Setup
*   Standard TTS: One voice (Siri).
*   Multi-Speaker TTS: 100 voices.
*   **Zero-Shot Cloning**: Give the model 3 seconds of *your* voice. It extracts your \"Speaker Embedding\".
*   It then conditions the generation on this embedding.
*   **Result**: The model reads text in YOUR voice.

## Task
1.  **Ethics**: This is dangerous (Deepfakes).
2.  **Watermarking**: Embed inaudible frequencies that identify the audio as AI-generated.
3.  **Task**: Use `VALL-E` or `Tortoise` to clone a voice (responsibly).

## Question
What is 'Grapheme-to-Phoneme' (G2P)?
*   Answer: Converting letters ("Colonel") to sounds ("Ker-nel"). English is non-phonetic. Spanish is phonetic. G2P models are critical for English TTS.
