# Audio Classification

## 1. Image Classification on Audio
*   Step 1: Convert Audio to Mel-Spectrogram (Image).
*   Step 2: Use ResNet-18 (CNN).
*   Step 3: Classify.
*   **Result**: It works surprisingly well. Dog barks look like vertical spikes. Police sirens look like horizontal lines.

## 2. Audio Event Detection (AED)
*   Difference between "Classification" and "Detection":
    *   **Classification**: "This 10-second clip is a Dog Bark."
    *   **Detection**: "The Dog barked at 0:03 and 0:07."
*   Models: YAMNet (Yet another Mobile Network), VGGish.

## 3. Keyword Spotting (KWS)
*   Specialized Classification: "Is this audio 'Hey Siri' or 'Random Noise'?"
*   Constraint: Must run 24/7 on low power.
*   Model: Tiny Depthwise Separable CNNs.
