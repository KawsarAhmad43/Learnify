# Research Project: Quantum Kernels (QML)

## 1. Problem Understanding
*   **Context**: Classification of data that is NOT linearly separable (e.g., Concentric Circles).
*   **Classical Solution**: SVM with RBF Kernel (maps to infinite dimensional space).
*   **Quantum Solution**: **Quantum Kernel**. Maps data into the Hilbert Space of a Quantum Processor.
*   **Hypothesis**: Quantum Feature Maps can find patterns RBF kernels miss (proven in some cryptographic datasets).

## 2. Research Strategy
*   **Simulator**: `PennyLane` (Easiest integration with PyTorch/Sklearn).
*   **Encode Data**: **Angle Embedding**. Map features $x_1, x_2$ to rotation angles of Qubits $\theta_1, \theta_2$.
*   **Feature Map**: **ZZFeatureMap**. Entangle Qubits to create non-linear correlations.
*   **Measure**: Calculate the overlap (fidelity) between two quantum states $|\phi(x)\rangle$ and $|\phi(x')\rangle$. This overlap IS the kernel value $K(x, x')$.
*   **Train**: Feed this Kernel Matrix into a standard `sklearn.svm.SVC`.

## 3. Step-by-Step Plan
1.  **Data**: `sklearn.datasets.make_circles`. Hard for linear classifiers.
2.  **Quantum Circuit**: Define a 2-Qubit circuit.
3.  **Kernel Calculation**: Compute the $N \times N$ matrix where entry $(i, j)$ is the similarity between Datapoint $i$ and Datapoint $j$ calculated on the QPU.
4.  **Training**: `svc = SVC(kernel="precomputed")`. Fit on the Quantum Kernel Matrix.
5.  **Viz**: Plot the decision boundary.
