# The CNN Data Pipeline

## 1. Beyond `model.fit()`
In the real world, you can't load all images into RAM (`numpy.load`). You need a **Pipeline**.
*   **Lazy Loading**: Open images one by one from disk only when needed.
*   **Preprocessing**: Resize/Normalise on the fly.
*   **Batching**: Group 32 images together.
*   **Prefetching**: While the GPU is training on Batch 1, the CPU prepares Batch 2.

## 2. Dataset vs DataLoader
*   **Dataset (The Map)**: knows *where* the data is and *how* to get one item (`__getitem__`).
*   **DataLoader (The Courier)**: Asks the Dataset for items, packages them into batches, and ships them to the GPU.

## 3. The Train/Val Split
*   Never train on everything.
*   Always split **File Paths** first, then create two separate datasets (TrainDataset, ValDataset).
*   This prevents "Data Leakage" (seeing the test set).
