# Linear Algebra for Machine Learning

Linear Algebra is the branch of mathematics concerning linear equations and their representations in vector spaces and through matrices. In ML, it is akin to the syntax of the language we use to describe data and models.

## Key Concepts

### 1. Vectors
A vector is an ordered list of numbers. In ML, a single data point is often represented as a vector of features.
*   **Geometric interpretation**: An arrow in space with magnitude and direction.
*   **Notation**: $\mathbf{x} \in \mathbb{R}^n$ means a vector with $n$ real numbers.

### 2. Matrices
A matrix is a 2D array of numbers.
*   **Data Matrix**: Rows correspond to samples, columns to features.
*   **Weights Matrix**: In Neural Networks, connections between layers are represented as matrices.

### 3. Dot Product
The dot product of two vectors $\mathbf{a}$ and $\mathbf{b}$ is $\sum a_i b_i$.
*   **Geometric Meaning**: $\mathbf{a} \cdot \mathbf{b} = ||\mathbf{a}|| ||\mathbf{b}|| \cos(\theta)$.
*   It measures **similarity**. If vectors point in the same direction, dot product is large. If orthogonal (90 degrees), it is 0.

### 4. Matrix Multiplication
If $A$ is $(m \times n)$ and $B$ is $(n \times p)$, their product $C = AB$ is $(m \times p)$.
*   Critical for Neural Network forward pass: $\mathbf{y} = W\mathbf{x} + \mathbf{b}$.

### 5. Eigenvectors and Eigenvalues
For a square matrix $A$, an eigenvector $\mathbf{v}$ satisfies $A\mathbf{v} = \lambda \mathbf{v}$.
*   When a linear transformation ($A$) is applied, the eigenvector does not change direction, only length (scaled by $\lambda$).
*   Used in **Principal Component Analysis (PCA)** to find the most important axes of data variance.
