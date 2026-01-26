# Advanced Retrieval

## 1. Hybrid Search
Vector search is great at concepts ("Cat" matches "Feline") but bad at exact keywords ("ID-123" matches "ID-124").
**Solution**: Combine Vector Search (Dense) + BM25/TF-IDF (Sparse).
*   Rank = $0.7 \times VectorScore + 0.3 \times BM25Score$.

## 2. Parent-Child Chunking
*   **Problem**: If you chunk a document into tiny 100-word pieces, the context ("Chapter 1") is lost.
*   **Solution**:
    *   Store small chunks (Children) for **Searching**. (Precise matches).
    *   Store large chunks (Parents) for **Generation**. (Rich context).
    *   When a Child is found, retrieve its Parent.

## 3. Query Expansion / Multi-Query
*   User asks: "How to fix wifi?"
*   LLM expands to: "Wifi troubleshooting steps", "Router reset guide", "ISP connectivity issues".
*   Search for ALL 3 variations and deduplicate results.
