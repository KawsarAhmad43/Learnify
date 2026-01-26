# Transformers and BERT

## 1. The Transformer (2017)
The paper "Attention is All You Need" killed RNNs.
*   **Parallelism**: Process the whole sentence at once (unlike RNNs which are sequential).
*   **Positional Encoding**: Since there is no sequence, we inject "position" info ($sin/cos$ waves) into the embeddings so the model knows word order.

## 2. BERT (Bidirectional Encoder Representations from Transformers)
*   **Encoder-Only**: Good at understanding.
*   **Masked Language Modeling (MLM)**: Hide 15% of words ("The [MASK] sat on the mat") and ask BERT to guess.
*   **Fine-Tuning**: Pre-train on Wikipedia (expensive), then fine-tune on your small dataset (cheap).

## 3. GPT (Generative Pre-trained Transformer)
*   **Decoder-Only**: Good at generating.
*   **Causal Language Modeling (CLM)**: Predict the next word.

## 4. The CLS Token
BERT adds a special `[CLS]` token at the start. The vector for this token learns to represent the **entire sentence**, making it perfect for classification.
