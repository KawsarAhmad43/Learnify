# Spectrograms and Signal Processing

## 1. Everything is a Wave
*   Audio = Air pressure changing over time.
*   **Sampling Rate**: 44.1kHz (CD Quality) means we measure pressure 44,100 times per second.

## 2. Fourier Transform (FFT)
*   Time Domain -> Frequency Domain.
*   It tells you: "This audio clip contains a lot of Low Bass and some High Treble".
*   Problem: It loses time. (It tells you *what* notes were played, but not *when*).

## 3. Spectrogram (STFT)
*   **Short-Time Fourier Transform**.
*   Chop the audio into tiny windows (e.g., 20ms).
*   Run FFT on each window.
*   Stack them.
*   **Result**: An **Image** where X-axis = Time, Y-axis = Frequency, Color = Intensity.
*   Now we can use CNNs (Computer Vision) on Audio!

## 4. Mel Scale
*   Humans hear pitch logarithmically. (Difference between 100Hz and 200Hz sounds huge. Difference between 10,000Hz and 10,100Hz sounds like nothing).
*   **Mel-Spectrogram**: A spectrogram warped to match human hearing. Input for almost all Deep Learning Audio models.
