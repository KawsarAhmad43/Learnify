# Text to Speech (TTS)

## 1. Components
*   **Text Analysis**: "Dr. Smith lives on St. John St." -> "Doctor Smith lives on Saint John Street". (Normalization).
*   **Acoustic Model**: "Hello" -> Mel-Spectrogram. (Tacotron 2).
*   **Vocoder**: Mel-Spectrogram -> Audio Waveform. (WaveNet / HiFi-GAN).

## 2. Concatenative vs Parametric vs Neural
*   **Concatenative**: Record a human reading 10,000 sentences. Chop them up. Glue them back together. (Old Siri. Sounded robotic but clear).
*   **Parametric**: Physics simulation of the throat. (Very robotic).
*   **Neural**: Learn the distribution of waveforms. (Indistinguishable from human).

## 3. Controllability
*   Modern TTS allows you to control **Prosody** (Emotion, Speed, Pitch).
*   Input: "Hello [Happy]", "Hello [Sad]".
