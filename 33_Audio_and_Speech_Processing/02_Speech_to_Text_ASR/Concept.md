# Speech to Text (ASR)

## 1. The Challenge
*   Audio: Continuous wave.
*   Text: Discrete characters.
*   Problem: "Hello" takes 0.5 seconds. "Heeeeello" takes 2.0 seconds. The number of input frames does not match the number of output characters.
*   We cannot just map Frame 1 -> 'H', Frame 2 -> 'e'.

## 2. CTC Loss (Connectionist Temporal Classification)
*   Allows the network to output "Blanks" ($\epsilon$).
*   Output: $H, H, H, \epsilon, \epsilon, e, e, l, l, l, l, o, \epsilon$.
*   Collapse repeats and remove blanks: "Hello".
*   This breakthrough allowed generic RNNs to do Speech Recognition without solving the alignment problem manually.

## 3. Whisper (OpenAI)
*   **Architecture**: Large Transformer (Encoder-Decoder).
*   **Data**: 680,000 hours of weakly labeled internet audio.
*   **Input**: Log-Mel Spectrogram.
*   **Output**: Text tokens.
*   **Features**: Multilingual, Translates, Robust to accents.
