# Research Project: Semantic Segmentation (U-Net)

## 1. Problem Understanding
*   **Context**: Analyzing Satellite Imagery (e.g., Identifying Water or Forest).
*   **Target**: Pixel-wise Classification. We don't just want to know "There is water", we need the exact boundary.
*   **Why Advanced?**: Standard CNNs (ResNet) shrink the image (pooling) to get a label. We need to shrink it to understand context, then **upsample** it back to full resolution to draw the map.

## 2. Research Strategy
*   **Architecture**: **U-Net**.
    *   **Encoder (Down)**: Captures "What" (Features). We use a pre-trained ResNet34 here (backbone).
    *   **Decoder (Up)**: Captures "Where" (Localization).
    *   **Skip Connections**: Concatenate Encoder features with Decoder features. This preserves fine details lost during pooling.
*   **Loss Function**: **Dice Loss** or **IoU** (Intersection over Union).
    *   Pixel accuracy is bad because 90% of the image might be background.
*   **Library**: `segmentation-models-pytorch`.

## 3. Step-by-Step Plan
1.  **Dataset**: 256x256 tiles of Satellite Images + Binary Masks.
2.  **Augmentation**: `albumentations`. Heavy transforms (Transpose, ElasticTransform) to simulate varied terrains.
3.  **Model**: `Unet(encoder_name="resnet34", encoder_weights="imagenet")`.
4.  **Training loop**: Predict mask -> Compare with Ground Truth using IoU -> Backprop.
5.  **Visualization**: Plot: Image | True Mask | Predicted Mask.
