# Task: Hallucination Check

## Objective
Detect unsupported claims.

## Setup
*   Context: \"The store is open from 9 AM to 5 PM.\"
*   Question: \"Is the store open at 8 PM?\"
*   Model Answer: \"No, it closes at 5 PM.\" -> **Grounded** (Good).
*   Model Answer: \"No, but we have an online store.\" -> **Hallucination** (Bad, context didn't mention online store).

## Task
1.  Why is the second answer bad?
    *   It might be true in the real world, but in a strict RAG system, assuming unretrieved information is dangerous (e.g., maybe the online store is down for maintenance).
2.  Goal: Force the model to say \"I don't know\" if the context is missing.

## Question
What is the 'Lost in the Middle' phenomenon?
*   Answer: If you paste 100 documents, LLMs tend to ignore the documents in the middle and focus only on the start/end. Reranking helps solve this.
