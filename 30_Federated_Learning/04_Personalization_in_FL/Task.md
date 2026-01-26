# Task: Energy Efficiency

## Objective
Green AI.

## Setup
*   Training on a phone drains battery.
*   Sending updates consumes Data Plan.
*   **System Design**: FL should only run when:
    1.  battery_level > 80%
    2.  is_charging == True
    3.  network_type == WiFi (unmetered)
    4.  phone_is_idle (Screen off)

## Task
1.  Implement these checks in your client code.
2.  **Model Compression**: Use Quantization (int8) before sending the model to reduce bandwidth by 4x.

## Question
What is 'Federated Unlearning'?
*   Answer: The Right to be Forgotten. If User X leaves the federation, how do we remove their contribution from the Global Model without retraining from scratch? (Very hard open problem).
