# Advanced Tricks by Data Type

## 1. Tabular Data
*   **Memory Optimization**: DataFrames often use `int64` or `float64` by default. Downcasting to `int8`, `int16`, or `float32` can save 70% of memory.
*   **High Cardinality Categoricals**: Use **Target Encoding** or **Frequency Encoding** instead of One-Hot to avoid exploding dimensions.
*   **Cyclical Features**: Encode hours (0-23) or months (1-12) using Sin/Cos transforms so 23 is close to 0.

## 2. Text Data (NLP)
*   **Tokenization**: Converting strings to lists of words.
*   **Stopwords**: Removing common words (the, a, is) that carry little meaning.
*   **TF-IDF**: Weighing words by how rare they are across documents, rather than just raw count.
*   **Lemmatization**: Converting "running", "ran", "runs" to the root "run".

## 3. Image Data (Computer Vision)
*   **Normalization**: Pixel values are 0-255. Divide by 255 to scale to [0, 1].
*   **Data Augmentation**: Randomly rotating, flipping, or zooming images to increase dataset size and robustness.
*   **Flattening**: Converting a 2D matrix (28x28) to a 1D vector (784) for dense layers.

## 4. Time Series
*   **Lag Features**: Using $y_{t-1}$ to predict $y_t$.
*   **Rolling Statistics**: Moving averages, moving standard deviations.
*   **Differencing**: Subtracting previous value to make non-stationary data stationary.
