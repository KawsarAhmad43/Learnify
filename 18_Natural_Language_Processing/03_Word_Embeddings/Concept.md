# Word Embeddings

## 1. The Sparse Problem
One-Hot Encoding (`[0, 1, 0, ...]`) is bad because:
*   **Huge**: Vocab size = 1,000,000? Vector is length 1M.
*   **Orthogonal**: "King" and "Queen" share no mathematics. Dot product is 0.

## 2. The Dense Solution (Embeddings)
Represent each word as a small vector (e.g., 300 dimensions) of float numbers.
*   **King**: `[0.2, 0.9, -0.4, ...]`
*   **Queen**: `[0.2, 0.95, -0.3, ...]`
*   **Similarity**: Now we can calculate Cosine distance!

## 3. Word2Vec (2013)
A shallow neural network trained to predict context.
*   **CBOW**: Predict "Fox" from "The Quick Brown [?] Jumps".
*   **Skip-Gram**: Predict "The, Quick, Brown" from "[Fox]".
*   **Result**: Words assuming similar contexts get similar vectors.

## 4. The Magic Algebra
$V(King) - V(Man) + V(Woman) \approx V(Queen)$
This suggests the model learned the "Gender" direction.
