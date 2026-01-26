# RAG Foundations

## 1. The Knowledge Cutoff Problem
LLMs are frozen in time.
*   GPT-4 doesn't know today's weather.
*   GPT-4 doesn't know your company's private emails.

## 2. Retrieval Augmented Generation (RAG)
**Analogy**: You (the LLM) are taking a test. You can browse a textbook (the Retriever) to find answers.
**Process**:
1.  **Retrieval**: Find relevant documents.
2.  **Augmentation**: Paste them into the prompt.
3.  **Generation**: Ask the LLM to answer using *only* that context.

## 3. The Prompt Template
"Answer the question based only on the following context:
{CONTEXT}
Question: {QUESTION}"

## 4. Why RAG?
*   **Traceability**: You can see exactly which document the AI used.
*   **Updater**: To update knowledge, just add a PDF to the folder. No re-training needed.
*   **Privacy**: Private data stays in your secure database, not in the model weights.
