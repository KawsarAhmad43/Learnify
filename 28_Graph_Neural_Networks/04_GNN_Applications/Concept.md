# GNN Applications

## 1. Node Classification
**Task**: Predict the label of a node.
*   **Example**: Fraud Detection.
*   **Graph**: Transactions. Nodes = Users/Merchants. Edges = Payments.
*   **Goal**: Label User X as "Fraudster" based on their connections to existing Frasudsters.

## 2. Link Prediction
**Task**: Predict if an edge *should* exist.
*   **Example**: Recommendation Systems.
*   **Graph**: Users and Products.
*   **Goal**: Predict probability of edge `(User_Alice, Product_iPhone)`. If high, show it in the feed.

## 3. Graph Classification
**Task**: Predict the label of the *entire* graph.
*   **Example**: Drug Discovery.
*   **Graph**: A Molecule (Nodes=Atoms, Edges=Bonds).
*   **Goal**: Is this molecule "Toxic" or "Safe"?
*   **Mechanism**: **Global Pooling**. After GCN layers, sum up ALL node embeddings to get one Graph Embedding vector.
