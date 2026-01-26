# Research Project: Federated Learning (FedAvg)

## 1. Problem Understanding
*   **Context**: Privacy constraints (GDPR/HIPAA). Hospital A cannot send X-Rays to Google. But they want a shared AI model.
*   **The Problem**: **Data Islands**.
*   **Solution**: Move the Model, not the Data.
    *   Server sends Model $\to$ Hospital A & B.
    *   Hospitals training locally on private data.
    *   Hospitals send updates (Gradients/Weights) back to Server.
    *   Server averages them (FedAvg).

## 2. Research Strategy
*   **Simulation**: We don't have 3 physical servers. We will simulate them using Python objects.
*   **Algorithm**: **FedAvg**.
    $$ W_{global} = \sum \frac{n_k}{n} W_k $$
    (Global weights = Weighted Average of Local weights).
*   **Challenge**: **Non-IID Data**.
    *   Hospital A only has Sick patients (Cancer Center).
    *   Hospital B only has Healthy patients (Wellness Clinic).
    *   FedAvg struggles here. We will simulate this by giving Client 1 only Class 0, and Client 2 only Class 1.

## 3. Step-by-Step Plan
1.  **Server**: A `GlobalModel` (Simple NN).
2.  **Clients**: 3 `Client` objects, each with a private `DataLoader`.
3.  **Communication Round**:
    *   Server broadcasts $W_0$.
    *   Client 1 performs 1 epoch of SGD. Returns $W_1$.
    *   Client 2 performs 1 epoch of SGD. Returns $W_2$.
    *   Server computes average. Updates $W_0$.
4.  **Evaluation**: Test the Global Model on a held-out test set covering ALL classes.
