# Machine Learning Paradigms & Notation

Before training models, you must speak the language of Machine Learning.

## 1. The Three Pillars
Most ML problems fall into three categories:

### A. Supervised Learning (The Teacher)
*   **Goal**: Learn a mapping from inputs $X$ to outputs $y$.
*   **Data**: Labeled datasets $\{(x^{(i)}, y^{(i)})\}$.
*   **Examples**:
    *   **Regression**: Predicting a continuous value (House Price).
    *   **Classification**: Predicting a category (Spam/Not Spam).
*   **Analogy**: A student learning from an answer key.

### B. Unsupervised Learning (The Explorer)
*   **Goal**: Find hidden structure or patterns in data.
*   **Data**: Unlabeled datasets $\{x^{(i)}\}$. No $y$.
*   **Examples**:
    *   **Clustering**: Grouping similar customers.
    *   **Dimensionality Reduction**: Compressing images.
*   **Analogy**: A baby learning to organize toys by shape without being told the names of the shapes.

### C. Reinforcement Learning (The Gamer)
*   **Goal**: Maximize a reward signal over time.
*   **Data**: Sequence of State-Action-Reward tuples.
*   **Examples**: Training a robot to walk, AlphaGo.
*   **Analogy**: Training a dog with treats.

## 2. Mathematical Notation (Standard)
We will use this notation throughout the course.

*   $m$: Number of training examples.
*   $n$: Number of features (input variables).
*   $\mathbf{x}^{(i)}$: The input vector of the $i$-th example (column vector).
*   $y^{(i)}$: The output (label) of the $i$-th example.
*   $X$: The Design Matrix ($m \times n$).
*   $\theta$ (Theta) or $w$: The weights/parameters of the model.
*   $h_\theta(x)$: The **Hypothesis** function. The model's prediction.
    *   Example Linear Model: $h_\theta(x) = \theta_0 + \theta_1 x_1 + \dots$

## 3. The Lifecycle
1.  **Problem Definition**: What are we solving?
2.  **Data Collection**: Constructing $X$ and $y$.
3.  **Training**: Finding the $\theta$ that minimizes error.
4.  **Inference**: Using $\theta$ to predict on new data.
