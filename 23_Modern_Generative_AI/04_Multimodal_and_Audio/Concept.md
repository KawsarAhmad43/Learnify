# Multimodal and Audio

## 1. CLIP: The Rosetta Stone
Contrastive Language-Image Pre-training (CLIP) maps Text and Images to the same shared space.
*   Embedding("A dog") $\approx$ Embedding(Photo of a dog).
*   embedding("A cat") $\neq$ Embedding(Photo of a dog).
This allows us to control image generation with text.

## 2. AudioLDM (Latent Diffusion for Audio)
Images are actually just Spectrograms (Time vs Frequency).
*   Convert Audio -> Spectrogram Image.
*   Train a standard Diffusion Model (like SD) on these Spectrograms.
*   Text Prompt: "Jazz saxophone solo".
*   Diffusion generates a "Jazz Spectrogram".
*   Vocoder (HiFi-GAN) converts Spectrogram back to Audio Waveform.

## 3. Multimodal alignment (ImageBind)
Meta's ImageBind aligns 6 modalities: Image, Text, Audio, Depth, Thermal, and IMU.
*   Embedding(Dog Barking) $\approx$ Embedding(Photo of Dog).
