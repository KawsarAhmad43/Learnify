# Quantum Support Vector Machines (QSVM)

## 1. The Kernel Trick
*   **Classical SVM**: Maps 2D data (not separable) to 3D space (separable by a hyperplane) using a Kernel Function $K(x, y)$.
*   **Problem**: Computing kernels for high-dimensional data is expensive.

## 2. Quantum Feature Maps
*   We can map classical data $x$ into a quantum state $|\Phi(x)\rangle$ using a quantum circuit.
*   This Hilbert space is exponentially large ($2^N$ dimensions).
*   **Quantum Kernel**: We compute the similarity as $K(x, y) = |\langle \Phi(x) | \Phi(y) \rangle|^2$.
*   This is known as the **Swap Test** or can be computed by runniing $U(x)$ then $U^\dagger(y)$ and measuring the probability of $|0\dots0\rangle$.

## 3. Advantage
*   If the Feature Map $U(x)$ is hard to simulate classically (e.g., involves complex entanglement), then the QSVM can potentially classify patterns that a classical SVM simply cannot "see".
