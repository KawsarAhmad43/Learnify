# Vision XAI

## 1. Saliency Maps / Sensitivity
"Where did the model look?"
*   Calculate the Gradient of the Output Class with respect to the Input Pixels.
*   $\nabla_x f(x)$.
*   If changing a pixel slightly changes the output drastically, that pixel is important.

## 2. Grad-CAM (Gradient-weighted Class Activation Mapping)
*   **Problem with Saliency**: It's too noisy (looks like static).
*   **Grad-CAM**: Instead of looking at Input Pixels, look at the **Last Convolutional Layer**.
    *   This layer captures high-level shapes (ears, noses).
    *   Take the gradients of the class "Tiger" w.r.t the feature maps.
    *   Result: A smooth heatmap over the tiger's face.

## 3. Integrated Gradients
*   Address the "Saturation" problem.
*   If a pixel is purely black (0), the gradient might be 0 even if it's important.
*   Method: Scale the image from Black -> Original in 50 steps. Sum the gradients at each step.
