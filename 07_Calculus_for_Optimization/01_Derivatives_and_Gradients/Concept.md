# Derivatives and Gradients

## 1. The Derivative
The derivative of a function $f(x)$ measures how sensitive the function's output is to small changes in its input $x$. Geometrically, it is the **slope** of the tangent line to the graph of $f$ at point $x$.

### Definition
$$f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}$$

## 2. Partial Derivatives
When a function depends on multiple variables (e.g., $f(x, y)$), we can look at how the function changes as we change just **one** variable, holding the others constant. These are called partial derivatives.
Notation: $\frac{\partial f}{\partial x}$ or $\partial_x f$.

## 3. The Gradient ($\nabla$)
The gradient is a vector that contains all the partial derivatives of a function.
For a function $f(x, y, z)$:
$$\nabla f = \begin{bmatrix} \frac{\partial f}{\partial x} \\ \frac{\partial f}{\partial y} \\ \frac{\partial f}{\partial z} \end{bmatrix}$$

### Key Property
The gradient vector points in the direction of the **steepest ascent** (greatest increase) of the function. Conversely, $-\nabla f$ points in the direction of **steepest descent**. This property is the foundation of Gradient Descent.

## 4. Jacobian and Hessian
*   **Jacobian Matrix**: The matrix of all first-order partial derivatives of a vector-valued function.
*   **Hessian Matrix**: A square matrix of second-order partial derivatives. It describes the local curvature of a function of many variables.
