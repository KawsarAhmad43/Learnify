# Research Project: Hybrid Transfer Learning (Feature Extraction)

## 1. Problem Understanding
*   **Context**: Using Deep Learning on non-deep datasets, or when compute is limited.
*   **Technique**: **Frozen Feature Extraction**. We don't train the CNN. We just use it as a "Lens" to see the image, then feed its description (Vector) to a Classical Model (XGBoost).
*   **Advantages**:
    *   **Speed**: Training XGBoost on vectors is 100x faster than Backprop on a CNN.
    *   **Data Efficiency**: Works better on small datasets (100-500 images) where CNNs overfit.

## 2. Research Strategy
*   **Backbone**: **VGG16** (Visual Geometry Group 16-layer model). Old but Gold. It produces very generalizable 4096-dimensional vectors from its FC1 layer.
*   **Classifier**: **XGBoost**. The king of tabular data. Here, the "Table" is the array of extracted vectors.
*   **Dimensionality Reduction**: 4096 is a lot of features for 500 images. We will try **PCA** to compress the embeddings before XGBoost.

## 3. Step-by-Step Plan
1.  **Data Sim**: Create a mock dataset of 2 classes (e.g. Cats vs Dogs) using random noise tensors (concept demo).
2.  **Extraction**: Pass images through VGG16 (pre-trained on ImageNet). Cut off the last layer.
3.  **Visualization**: Use t-SNE to see if VGG16 separates the classes naturally (Zero-Shot clustering).
4.  **Training**: Fit XGBoost on the vectors.
5.  **Evaluation**: Compare against a Raw CNN trained from scratch (which should fail/overfit on small data).
