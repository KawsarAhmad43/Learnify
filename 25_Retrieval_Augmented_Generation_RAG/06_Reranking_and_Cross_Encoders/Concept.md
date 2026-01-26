# Reranking and Cross-Encoders

## 1. Bi-Encoder (Retriever)
*   **Method**: Pre-calculate `Embedding(Doc)`. Calculate `Embedding(Query)` at runtime. `Score = DotProduct`.
*   **Speed**: Insanely fast (MIPS).
*   **Con**: The interaction between Query and Doc is simple vector alignment. It misses nuance.

## 2. Cross-Encoder (Reranker)
*   **Method**: Feed `[CLS] Query [SEP] Document` into BERT.
*   **Mechanism**: The attention mechanism allows words in the Query to "talk" directly to words in the Document.
*   **Score**: Output of a classification head (0 to 1).
*   **Speed**: Slow. Requires a full BERT forward pass for EACH document pair.
*   **Pro**: Much higher accuracy.

## 3. The Perfect Combo
Use Bi-Encoder to find the Top 100 candiates (Recall).
Use Cross-Encoder to sort the Top 100 and pick the Top 5 (Precision).
