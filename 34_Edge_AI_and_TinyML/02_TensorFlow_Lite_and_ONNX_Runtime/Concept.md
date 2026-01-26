# TensorFlow Lite and ONNX Runtime

## 1. The Fragmentation Problem
*   Training: PyTorch / TensorFlow (Python).
*   Deployment: Android (Java/Kotlin), iOS (Swift), Web (JavaScript), IoT (C++).
*   We cannot install PyTorch (2GB) on an Apple Watch.

## 2. Standard Formats
*   **ONNX (Open Neural Network Exchange)**: A common format. Convert PyTorch -> ONNX -> Run anywhere (C++, C#, Java).
*   **TFLite**: Google's flatbuffer format for mobile. Optimized for ARM CPUs and Mobile GPUs.

## 3. The Converter
*   **Step 1**: Train model in Python.
*   **Step 2**: Freeze Graph (Merge weights and architecture).
*   **Step 3**: Optimize (Fuse layers: Conv + ReLU -> ConvReLU).
*   **Step 4**: Serialize to `.tflite` or `.onnx` file.
