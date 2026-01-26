# Text Preprocessing

## 1. Computers Don't Read
Computers only understand numbers. To feed text into a neural network, we must clean it and break it down.

## 2. Tokenization
Splitting a sentence into units (Tokens).
*   **Word-level**: "I love AI" -> ["I", "love", "AI"]
*   **Character-level**: "AI" -> ["A", "I"]
*   **Subword-level**: "Smartest" -> ["Smart", "est"] (Used by BERT/GPT).

## 3. Cleaning Steps
*   **Lowercasing**: "Apple" == "apple".
*   **Stop Words**: Removing common words like "the", "is", "at" that carry little meaning.
*   **Stemming/Lemmatization**: Reducing words to their root.
    *   **Stemming**: Chopping off ends ("Running" -> "Runn"). Fast but dumb.
    *   **Lemmatization**: Dictionary lookup ("Better" -> "Good"). Slow but smart.

## 4. Normalization
Cleaning up noise (HTML tags, URLs, Emojis) depending on the task.
