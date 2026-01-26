# Task: Extraction Cost

## Objective
The price of structure.

## Setup
*   1 Million Documents.
*   To build the graph, an LLM must read EVERY document to extract entities.
*   Cost per document: $0.01 (GPT-4o-mini).

## Task
1.  Total Cost: $1,000,000 \times 0.01 = 10,000$.
2.  Vector Index Cost: Embedding 1M docs is ~$50.
3.  Ratio: GraphRAG is 200x more expensive to *build* than Vector RAG.

## Question
Is it worth it?
*   Answer: Only for \"Global\" questions (\"Summarize the prompt\") or \"Multi-hop\" questions. For simple lookup (\"What is the leave policy?\"), Graphs are overkill.
