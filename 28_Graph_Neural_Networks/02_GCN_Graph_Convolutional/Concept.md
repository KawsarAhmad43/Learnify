# Graph Convolutional Networks (GCN)

## 1. Message Passing
How to learn from neighbors?
*   Step 1: Each node sends its features to its neighbors.
*   Step 2: Receiving node sums (aggregates) the messages.
*   Step 3: Update node state using a Neural Net (Weight Matrix $W$).
*   Formula: $H^{(l+1)} = \sigma( \hat{D}^{-1/2} \hat{A} \hat{D}^{-1/2} H^{(l)} W^{(l)} )$

## 2. Receptive Field
*   **1 Layer GCN**: I know my immediate friends.
*   **2 Layer GCN**: I know my friends' friends. (2 Hops).
*   **Deep GCNs**: Usually stick to 2-3 layers. Going too deep causes "Over-smoothing" (Everyone's features average out to the same blob).

## 3. Spectral vs Spatial
*   **Spectral**: Based on Graph Fourier Transform (Eigenvalues of Laplacian). Mathematically beautiful but hard to scale.
*   **Spatial**: Message passing (Direct summation). Easier to implement and scale. (Modern GCNs are Spatial).
