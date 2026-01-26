# Knowledge Graph RAG

## 1. The Vector Limitation
Vectors connect "Apples" to "Fruit".
Vectors FAIL to connect "Alice" to "Bob" if the text never explicitly mentions them together in one chunk.
Relationship: `Alice --works_for--> Acme <--works_for-- Bob`.
A vector search for "Alice's colleague" might fail. A Graph search will succeed (2 hops).

## 2. GraphRAG
1.  **Extract**: Use an LLM to read documents and output Triples (`Entity A -> Relation -> Entity B`).
2.  **Store**: Put Triples in Neo4j.
3.  **Query**:
    *   Find "Alice".
    *   Traverse 2 hops.
    *   Retrieve "Bob".
    *   Feed both to LLM.

## 3. Microsoft GraphRAG
A specific technique that creates "Communities" of nodes.
*   Cluster the graph.
*   Summarize each cluster ("This cluster represents the Engineering Team").
*   Allows "Global" questions: "What are the main themes in this dataset?" (Impossible with standard RAG).
