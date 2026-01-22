# Chain Rule and Backpropagation

## 1. Composite Functions
Complex models (like Neural Networks) are essentially giant composite functions:
$$y = f(g(h(x)))$$
To find how $y$ changes with respect to $x$, we need the Chain Rule.

## 2. The Chain Rule
If $z = f(y)$ and $y = g(x)$, then:
$$\frac{dz}{dx} = \frac{dz}{dy} \cdot \frac{dy}{dx}$$

In the context of Partial Derivatives:
If $z = f(u, v)$ where $u = g(x, y)$ and $v = h(x, y)$, then:
$$\frac{\partial z}{\partial x} = \frac{\partial z}{\partial u}\frac{\partial u}{\partial x} + \frac{\partial z}{\partial v}\frac{\partial v}{\partial x}$$

## 3. Computational Graphs
A computational graph represents a mathematical expression as a directed graph.
*   **Nodes**: Operations or variables.
*   **Edges**: Data flow.

## 4. Backpropagation
Backpropagation is simply **applying the Chain Rule repeatedly** on a computational graph, starting from the output (Loss) and working backward to the inputs (Weights).

### Steps:
1.  **Forward Pass**: Compute values from input to output.
2.  **Backward Pass**: Compute local gradients and multiply them (chain rule) traversing from right to left.
    *   `Global Gradient = Upstream Gradient * Local Gradient`
