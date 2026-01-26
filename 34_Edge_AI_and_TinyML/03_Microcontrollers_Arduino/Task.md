# Task: Sensor Fusion

## Objective
More data, less noise.

## Setup
*   **Sensor 1 (Accelerometer)**: Drifts over time. Good for short movements.
*   **Sensor 2 (GPS)**: Accurate position, but slow update rate (1Hz) and high power.
*   **Sensor 3 (Magnetometer)**: Gives direction, but affected by metal objects.

## Task
1.  **Kalman Filter**: The classical way to fuse these.
2.  **Neural Fusion**: Train a small RNN that takes inputs from *all* sensors and outputs the true state (Position/Velocity).
3.  **Task**: Run a simple Gesture Recognition model (Magic Wand) that recognizes if you wave the Arduino in a \"W\" shape.

## Question
What is 'Edge Impulse'?
*   Answer: A web platform that makes TinyML easy. You connect your device, record data in the browser, train in the cloud, and download the C++ library.
