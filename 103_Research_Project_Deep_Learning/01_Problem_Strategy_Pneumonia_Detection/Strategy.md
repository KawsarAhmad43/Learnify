# Research Project: Pneumonia Detection (Deep Learning)

## 1. Problem Understanding
*   **Context**: Helping radiologists detect Pneumonia in Chest X-Rays.
*   **The Data**: [Chest X-Ray Images (Pneumonia)](https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia).
    *   2 Categories: NORMAL vs PNEUMONIA.
    *   Imbalance: More Pneumonia cases than Normal (unusual, usually it's the reverse).
*   **Challenge**: Small dataset (~5k images). Training a CNN from scratch will overfit instantly.

## 2. Research Strategy
*   **Transfer Learning**: Use **ResNet50** or **EfficientNet** pretrained on ImageNet.
    *   The model already knows how to detect edges, curves, and textures. We just need to teach it what "lungs" look like.
    *   **Freeze** the base layers, train only the final `Dense` layer (Head).
*   **Data Augmentation**:
    *   X-Rays can be rotated slightly, zoomed, or brightness changed.
    *   Warning: Do NOT flip horizontally (Heart is on the left side. Flipping creates a situs inversus patient).
*   **Explainability (Grad-CAM)**:
    *   A black box model is dangerous in medicine.
    *   We produce a "Heatmap" showing WHICH part of the image triggered the "Pneumonia" prediction.

## 3. Step-by-Step Plan
1.  **Loader**: Use `ImageDataGenerator` or PyTorch `DataLoader` with augmentations.
2.  **Model**: Load ResNet50 (include_top=False). Add GlobalAveragePooling -> Dense(1, sigmoid).
3.  **Training**: Use `BinaryCrossentropy`. Monitor `val_loss`. Use EarlyStopping.
4.  **Fine-Tuning**: Unfreeze the last 10 layers of ResNet and retrain with a very low learning rate (1e-5).
5.  **Grad-CAM**: Pass an image, get gradients of the final Convolutional layer, multiply maps by gradients to get the heatmap.
