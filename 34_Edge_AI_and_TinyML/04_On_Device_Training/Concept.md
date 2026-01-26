# On-Device Training

## 1. Inference vs Training
*   **Inference**: Running `y = f(x)`. Cheap.
*   **Training**: Running `y = f(x)`, computing gradients, updating weights. Expensive (Requires storing Activations for Backprop).

## 2. Why Train on Device?
*   **Privacy**: "Federated Learning" happens here.
*   **Personalization**: Face ID learns *your* face changes over time (Beard, Glasses). It doesn't send your face to Apple.
*   **Adaptation**: An anomaly detector learns the "Normal Vibration" of the specific washing machine it is attached to.

## 3. Transfer Learning
*   We rarely train from scratch on a phone.
*   We download a frozen "Backbone" (ResNet).
*   We only train the "Head" (Last Layer).
*   This matches the compute capability of modern phones.
