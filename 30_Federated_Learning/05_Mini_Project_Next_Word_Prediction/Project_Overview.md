# Mini Project: Federated Next Word Prediction

This project simulates a **Federated Learning** system where 3 distinct users train a shared global model to predict the next word in a sentence, **without sharing their data**.

## Structure
*   `dataset.py`: Creates private local datasets for each user.
*   `model.py`: Defines the simple Neural Network (simulated).
*   `client.py`: Handles local training (SGD) on private data.
*   `server.py`: Handles aggregation (FedAvg).
*   `run_simulation.py`: Orchestrates the FL rounds.

## The Users
1.  **User 1 (Sports Fan)**: "I love [soccer]", "The score is [high]"
2.  **User 2 (Foodie)**: "I love [pizza]", "The taste is [good]"
3.  **User 3 (Techie)**: "I love [python]", "The code is [slow]"

## Goal
The Global Model should learn the structure "I love [NOUN]" and "The [NOUN] is [ADJ]", adapting to the aggregate vocabulary of all users, without ever seeing a single localized dataset.
