# Classic Architectures (The Hall of Fame)

## 1. LeNet-5 (1998)
*   **Input**: 32x32 Gray.
*   **Structure**: Conv -> Pool -> Conv -> Pool -> Dense.
*   **Significance**: Proved CNNs work for digits (MNIST).

## 2. AlexNet (2012)
*   **Input**: 227x227 Color.
*   **Significance**: The "Deep" Revolution. Used ReLU and Dropout for the first time. Trained on GPUs.

## 3. VGG-16 (2014)
*   **Philosophy**: "Make it deeper and simpler."
*   **Design**: Used *only* 3x3 convolutions stacked on top of each other.
*   **Blocks**: Conv-Conv-Pool repeated many times.
*   **Downside**: Extremely heavy (138 Million parameters).

## 4. Why 3x3 Filters?
*   Two 3x3 filters have the same "Field of View" (Receptive Field) as one 5x5 filter.
*   But they have fewer parameters ($3^2+3^2 = 18$ vs $5^2 = 25$) and more non-linearity (2 ReLUs vs 1).
