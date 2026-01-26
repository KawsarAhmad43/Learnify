# Transfer Learning & Augmentation

## 1. Don't Be a Hero (Use Pre-trained Models)
Training a CNN from scratch requires:
*   Millions of images.
*   Weeks of GPU time.
*   Ph.D. level hyperparameter tuning.

**Transfer Learning**: Take a model trained on ImageNet (1000 classes) and repurpose it for your "Hot Dog vs Not Hot Dog" app.
*   **Feature Extraction**: Freeze the convolutional base (the "eye"). Re-train only the top Dense layer (the "brain").
*   **Fine-Tuning**: Unfreeze a few top layers and train gently (low LR) to adapt the features to your specific data.

## 2. Data Augmentation (Fake It 'Til You Make It)
If you only have 100 images, your model will overfit.
*   **Augmentation**: Generate new training samples on the fly.
    *   Rotate 15 degrees.
    *   Flip Horizontal.
    *   Zoom in/out.
*   This teaches the model **invariance** (a cat is still a cat if it's upside down).
