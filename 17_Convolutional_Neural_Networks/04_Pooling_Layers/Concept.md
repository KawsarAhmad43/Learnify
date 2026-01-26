# Pooling Layers

## 1. What is Pooling?
Pooling (Downsampling) reduces the size of the feature maps.
*   **Goal**: Reduce computational cost and prevent overfitting.
*   **Invariant**: Small shifts in the input shouldn't change the output. Pooling makes the network "Translation Invariant".

## 2. Types of Pooling
### Max Pooling
*   Takes the **Maximum** value in the window.
*   **Why?** Keeps the strongest feature (e.g., "There is definitely an edge here!").
*   Most common.

### Average Pooling
*   Takes the **Average** value.
*   **Why?** Keeps background information. Less common now (except at end of network).

## 3. Global Average Pooling (GAP)
*   Takes the average of the **entire** feature map (e.g., 7x7 -> 1x1).
*   Used instead of Flattening to connect Convolutional base to Dense Layers.
