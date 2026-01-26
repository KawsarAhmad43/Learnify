# Research Project: Private RAG (Retrieval Augmented Generation)

## 1. Problem Understanding
*   **Context**: A Law Firm wants to ask questions to their PDF archive. "What is the termination clause in the 2023 Agreement?".
*   **Constraint**: Confidentiality. Data CANNOT leave the on-premise server. No OpenAI API. No Cloud.
*   **The Trap**: "Hallucinations". If the LLM doesn't know the answer, it makes one up. RAG fixes this by grounding the AI in facts.

## 2. Research Strategy
*   **Ingestion**: PyPDFLoader (LangChain).
*   **Chunking Strategy**: A legal contract is 50 pages. We can't feed all 50 pages to a small LLM context window.
    *   **RecursiveCharacterTextSplitter**: Split by paragraphs (double newline), then sentences.
    *   **Chunk Overlap**: Keep 200 characters overlap so we don't cut a sentence in half.
*   **Embeddings**: `sentence-transformers/all-MiniLM-L6-v2`. Small, fast, accurate. Runs on CPU.
*   **Retrieval**:
    *   **Vector Search (KNN)**: Good for semantic similarity.
    *   **Keyword Search (BM25)**: Good for exact matches (Case IDs).
    *   **Hybrid Search**: The best of both.
*   **Generation**: `Llama-3-8B-Instruct` (Quantized to 4-bit using `bitsandbytes` to fit on a consumer GPU).

## 3. Step-by-Step Plan
1.  **Load PDFs**: Simulate a folder of legal docs.
2.  **Vector Store**: Use ChromaDB (persistent local DB).
3.  **Retriever**: Configure it to return `k=3` chunks.
4.  **Prompt Engineering**: "You are a helpful legal assistant. Use ONLY the following context to answer the question. If you don't know, say 'I don't know'."
5.  **Chain**: Combine Retriever + Prompt + LLM.
