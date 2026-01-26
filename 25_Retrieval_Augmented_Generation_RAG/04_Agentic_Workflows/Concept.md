# Agentic RAG

## 1. Naive RAG is Blind
Naive RAG *always* retrieves, even if the user says "Hi".
Naive RAG *never* validates the retrieval.
**Agentic RAG**: Adds a "Brain" (Controller) to the process.

## 2. Router
The Controller looks at the query and decides:
*   "Hi" -> Chat Mode (No RAG).
*   "What is our revenue?" -> SQL Tool.
*   "How does the new policy affect me?" -> Vector DB Tool.

## 3. Self-RAG (Reflection)
1.  **Retrieve**: Get docs.
2.  **Critique**: Ask LLM "Are these docs actually relevant?". If No, searches again with a rewritten query.
3.  **Generate**: Write answer.
4.  **Critique**: Ask LLM "Is this answer supported by the docs?".

## 4. Multi-Step Reasoning
"Compare the revenue of 2023 vs 2024".
*   Step 1: Retrieve 2023 Revenue.
*   Step 2: Retrieve 2024 Revenue.
*   Step 3: Calculate difference.
Naive RAG would try to find one document that contains the comparison, which might not exist.
