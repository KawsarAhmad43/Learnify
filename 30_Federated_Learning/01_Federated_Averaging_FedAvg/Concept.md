# Federated Averaging (FedAvg)

## 1. The Core Idea
*   **Traditional ML**: "Move Data to Code" (Upload everything to the Cloud).
*   **Federated ML**: "Move Code to Data" (Download the model to the Phone).

## 2. The Process
1.  **Initialize**: Server creates a global model $W_G$.
2.  **Broadcast**: Server sends $W_G$ to 100 random users (Clients).
3.  **Local Training**: Each client trains $W_G$ on their own SECRET data (e.g., text messages) for 5 epochs. They get a local model $W_L$.
4.  **Upload**: Clients verify the update $\Delta W = W_L - W_G$ (only the weights, not data) back to the server.
5.  **Aggregation**: Server averages the updates: $W_G^{new} = W_G + \frac{1}{N} \sum \Delta W$.
6.  **Repeat**.

## 3. Communication Cost
The bottleneck is WiFi.
*   Models are large (1GB).
*   We can't do this every second. We do it when the phone is **Plugged In and on WiFi**.
