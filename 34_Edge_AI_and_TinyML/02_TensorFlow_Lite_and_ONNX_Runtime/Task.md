# Task: Interpreters

## Objective
The engine.

## Setup
*   The `.tflite` file is just data (weights).
*   You need code to *read* and *execute* it.
*   **Interpreter**: A tiny C++ library that loads the file and runs the math.

## Task
1.  **Delegate**: By default, the interpreter runs on the CPU.
2.  **GPU Delegate**: Tell the interpreter to offload matrix multiplications to the GPU (OpenGL/Vulkan).
3.  **NNAPI Delegate**: Tell it to use the Android Neural Networks API (NPU).
4.  **Task**: Compare inference speed with different delegates. CPU: 100ms. GPU: 20ms.

## Question
What is 'Unsupported Operator'?
*   Answer: The nightmare of Edge AI. You used `torch.fft` in your model. TFLite doesn't support FFT. The converter throws an error. You must implement the FFT manually in C++ or change your model architecture.
