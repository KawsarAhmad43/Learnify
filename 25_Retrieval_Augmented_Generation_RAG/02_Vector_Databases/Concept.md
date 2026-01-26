# Vector Databases

## 1. Embeddings: The Core
Text is hard to compare.
*   "King" vs "Queen". (Are they close? Yes).
*   "Queen" vs "Car". (Are they close? No).
*   **Embedding Model** (e.g., OpenAI text-embedding-3): Converts text to a vector (array of 1536 floats).
*   In this vector space, `Distance(King, Queen)` is tiny.

## 2. Approximate Nearest Neighbor (ANN)
If you have 1 Billion Documents, comparing a query to EVERY document ($O(N)$) is too slow.
**Solutions**:
*   **HNSW (Hierarchical Navigable Small World)**: A graph-based index. "Six Degrees of Kevin Bacon" for data points.
*   **IVF (Inverted File)**: Clustering.
*   These algorithms find the nearest neighbors in $O(\log N)$ time.

## 3. Vector DBs
*   **Purpose-Built**: Chroma, Pinecone, Milvus, Weaviate.
*   **SQL Extensions**: pgvector (PostgreSQL).
*   They store the Vectors + Metadata + Original Text.
