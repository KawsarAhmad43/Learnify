# Feature Extraction (Classic)

## 1. Bag of Words (BoW)
Converting text into a fixed-length vector by counting word occurences.
*   **Corpus**: "I love AI", "I love code".
*   **Vocab**: ["I", "love", "AI", "code"]
*   **Vector 1**: [1, 1, 1, 0]
*   **Vector 2**: [1, 1, 0, 1]
*   **Problem**: "I" appeared 500 times? It dominates the vector, but carries no meaning.

## 2. TF-IDF
**Term Frequency - Inverse Document Frequency**.
*   **Goal**: Downscale words that appear everywhere (like "the", "a"). Upscale rare words (like "Quantum").
*   $TF = Count(word)$
*   $IDF = \log(\frac{Total Docs}{Docs with word})$
*   $Score = TF \times IDF$

## 3. Sparse Matrices
Most vectors are mostly zeros. Storing `[0, 0, 0, 1, 0 ...]` is wasteful.
*   **Sparse Matrix**: Only store `(index: 3, value: 1)`.
