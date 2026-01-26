# The NLP Data Pipeline

## 1. Text is Variable Length
Images are always a fixed grid (e.g., 224x224). Text varies.
*   Tweet: "Hi" (1 token).
*   Book: "It was the best of times..." (100k tokens).
*   **Batching Problem**: A matrix must be rectangular. You can't stack a length-2 vector with a length-100 vector.

## 2. Padding
We force everything to be the same size by adding zeros (PAD tokens).
*   "Hi" -> [101, 0, 0, 0]
*   "Hello World" -> [202, 303, 0, 0]
*   **Masking**: We must tell the Attention mechanism to *ignore* the zeros (Attention Mask: [1, 1, 0, 0]).

## 3. Dynamic Padding (Bucket Batching)
Padding to the max length of the *entire dataset* is wasteful.
*   **Smart approach**: Pad to the max length of the *current batch*.
*   If a batch has short sentences, the matrix is small (fast).
*   If a batch has long sentences, the matrix is big (slow).

## 4. The Tokenizer
The bridge between Human (String) and Machine (Integer).
*   Handles vocabulary lookup and special tokens (`[CLS]`, `[SEP]`, `[PAD]`).
