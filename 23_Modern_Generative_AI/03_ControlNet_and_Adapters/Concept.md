# ControlNet and Adapters

## 1. The Problem with Prompts
"Generate a man standing in a T-pose."
Stable Diffusion might give you a man sitting, or walking.
Text is a terrible way to describe geometry.

## 2. ControlNet Solution
Don't retrain Stable Diffusion.
1.  **Clone** the U-Net Encoder.
2.  **Freeze** the original U-Net.
3.  Calculated a "Zero Convolution" to merge the Clone features back into the Original.
4.  Train **ONLY** the Clone on (Image, Structure) pairs.
    *   Structure = Canny Edge, Human Pose Skeleton, Depth Map.

## 3. How it Works
*   The Original SD knows "What a man looks like".
*   The ControlNet Clone knows "Where the edges are".
*   They combine to generate "A man" (SD) exactly "on these edges" (ControlNet).

## 4. Adapters (T2I-Adapter, IP-Adapter)
Lighter versions of ControlNet.
*   **IP-Adapter (Image Prompt)**: Instead of text, feed an image. "Generate a cat that looks like *this specific cat*".
