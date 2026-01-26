# RAG Evaluation (RAGAS)

## 1. The Vibe Check
"Does this answer look good?" is not a metric.
You need numbers to optimize your system.

## 2. The RAG Triad
We need to evaluate three links:
1.  **Context Relevance**: Is the retrieved document actually relevant to the query? (Retriever Quality).
2.  **Faithfulness**: Is the answer derived *only* from the retrieved context? (Hallucination Check).
3.  **Answer Relevance**: Does the answer actually address the user's query? (End-to-End Quality).

## 3. RAGAS (RAG Assessment)
A framework that uses *another* LLM (like GPT-4) as a Judge to score these metrics on a scale of 0.0 to 1.0.
*   **Prompt**: "Given the Context and the Answer, count how many claims in the Answer are supported by the Context. Score = Supported / Total."
