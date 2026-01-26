# Microcontrollers (Arduino/ESP32)

## 1. The Constraints
*   **Memory**: 256 *Kilobytes* of RAM. (Not Gigabytes).
*   **Storage**: 1 Megabyte of Flash.
*   **Clock**: 80 MHz.
*   **OS**: None (Bare metal C++).

## 2. TinyML
*   We cannot run Linux or Python.
*   We compile the model into a C++ Byte Array.
*   We use `TensorFlow Lite for Microcontrollers` (TFLM).
*   It has no dynamic memory allocation (`malloc`). All tensors are pre-allocated in a static "Arena".

## 3. Sensors
*   TinyML is useless for generic internet data.
*   It is POWERFUL for sensor data: "Is this motor vibrating strangely?" (Accelerometer). "Did someone say 'Help'?" (Microphone).
