# Few-Shot and Zero-Shot Learning

## 1. The Human Ability
If I show you a picture of a "Quokka" (a rare animal) for the first time, you can instantly recognize another Quokka.
Standard Deep Learning needs 1,000 photos. Humans need 1.
*   **Zero-Shot**: Classify without seeing ANY examples (CLIP).
*   **One-Shot**: Classify after seeing 1 example.
*   **Few-Shot**: Classify after seeing 2-5 examples.

## 2. Metric Learning (Prototypical Networks)
Instead of learning "Classes" (Dog, Cat), we learn a "Distance Metric".
*   Network outputs a vector $f(x)$.
*   We want $Distance(f(x_1), f(x_2))$ to be small if they are the same class.
*   **Class Prototype**: The mean of the support set vectors: $c_k = \frac{1}{N} \sum f(x_i)$.
*   **Classification**: Measuring distance to the Prototype.

## 3. N-Way K-Shot
*   **N-Way**: How many classes are we choosing between? (e.g., Cat vs Dog vs Bird = 3-Way).
*   **K-Shot**: How many examples per class do we have? (e.g., 5 photos each = 5-Shot).
