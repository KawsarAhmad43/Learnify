# Task: Data Augmentation

## Objective
Robustness.

## Setup
*   Training on clean audio fails in the real world (Traffic noise, Room reverb).
*   **SpecAugment**: A famous augmentation technique by Google Brain.
*   Instead of augmenting the audio (adding noise), we augment the **Spectrogram Image**.

## Task
1.  **Time Masking**: Draw a black vertical bar on the spectrogram (Delete a chunk of time).
2.  **Frequency Masking**: Draw a black horizontal bar (Delete a specific frequency, e.g., Bass).
3.  **Result**: The model learns to recognize the word even if part of it is missing or corrupted.

## Question
What is 'MFCC'?
*   Answer: Mel-Frequency Cepstral Coefficients. An older, compressed version of Mel-Spectrograms (typically only 13 coefficients). Used in old speech systems (HMMs). Deep Learning prefers the full Mel-Spectrogram (more information).
