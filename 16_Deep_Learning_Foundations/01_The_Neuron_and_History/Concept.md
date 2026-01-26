# The Neuron and History

## 1. The Inspiration: Biological Neurons
Deep Learning is loosely inspired by the human brain.
*   **The Brain**: A massive network of ~86 billion neurons connected by synapses.
*   **The Signal**: A neuron touches thousands of other neurons. It receives electrical signals (inputs), sums them up, and if the charge is strong enough, it "fires" (outputs) a signal to its neighbors.
*   **Learning**: "neurons that fire together, wire together." (Hebb's Law). The brain learns by strengthening or weakening connections.

## 2. The Artificial Neuron (Perceptron)
The mathematical version of a biological neuron.
*   **Inputs ($x$)**: Data features (e.g., pixel brightness).
*   **Weights ($w$)**: The "strength" of the connection (importance).
*   **Bias ($b$)**: A threshold to trigger activation.
*   **Activation Function**: The decision rule (fire or don't fire?).

### The Formula
$$ z = (w_1 x_1 + w_2 x_2 + ... + w_n x_n) + b $$
$$ y = Activation(z) $$

## 3. A Brief History of Deep Learning
*   **1958 (The Perceptron)**: Frank Rosenblatt invents the Perceptron. It could learn simple linear patterns.
*   **1969 (The AI Winter)**: Minsky and Papert proved Perceptrons couldn't solve XOR (non-linear problems). Funding froze.
*   **1986 (Backpropagation)**: Hinton and others popularized Backprop, allowing multi-layer networks to learn.
*   **2012 (AlexNet)**: Deep Learning crushed the ImageNet competition (computer vision), powered by GPUs. Results improved from 74% to 85% accuracy instantly.
*   **2017 (Transformers)**: "Attention is All You Need" changed NLP forever (BERT, GPT).

## 4. Why Now?
1.  **Big Data**: We have internet-scale datasets to train massive models.
2.  **Hardware (GPUs)**: Matrix multiplication is parallelizable. NVIDIA GPUs made training 100x faster.
3.  **Better Algorithms**: ReLU, Adam, Residual connections resolved vanishing gradients.
