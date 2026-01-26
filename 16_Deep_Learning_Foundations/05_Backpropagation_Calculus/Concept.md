# Backpropagation & Calculus

## 1. The Blame Game
When the network makes a mistake (High Loss), who is to blame?
*   Did the output layer mess up?
*   Or did the hidden layer give bad information?
*   Or did the first layer fail to detect the edges?
**Backpropagation** answers this by calculating how much each weight contributed to the error.

## 2. The Chain Rule (The Engine of Backprop)
If $y = f(u)$ and $u = g(x)$, then:
$$ \frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx} $$

### In Neural Networks
$$ Loss = L(Prediction) $$
$$ Prediction = f(Weight \cdot Input) $$
We want to change the Weight to lower the Loss.
$$ \frac{\partial Loss}{\partial Weight} = \frac{\partial Loss}{\partial Prediction} \cdot \frac{\partial Prediction}{\partial Weight} $$
We chain these derivatives from the end (Output) back to the beginning (Input).

## 3. Computational Graphs
We visualize the math as a graph.
*   Nodes = Operations (+, *, Sigmoid)
*   Edges = Values flowing
*   **Forward**: Calculate values.
*   **Backward**: Calculate gradients (local gradient * upstream gradient).
