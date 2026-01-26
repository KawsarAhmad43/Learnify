# Task: Edge Features?

## Objective
Beyond nodes.

## Setup
*   Social network: Edge (Friendship) has feature \"Years Known\".
*   Road network: Edge (Road) has feature \"Distance\".
*   Standard GCN ignores edge features (only uses node features).

## Task
1.  How to incorporate Edge Features?
2.  **GAT Solution**: The attention score $\alpha_{ij}$ is partially derived from the edge attributes.
    *   $e_{ij} = \text{LeakyReLU}(a^T [Wh_i || Wh_j || \text{EdgeFeat}_{ij}])$.
3.  This allows the model to learn: \"If Years Known > 10, pay high attention.\"

## Question
Why is GAT more computationally expensive than GCN?
*   Answer: GCN is static matrix multiplication. GAT requires computing pairwise scores for every edge, every epoch.
