# Model Training and Evaluation

## 1. The Experiment
*   **Baseline**: Start simple. Linear Regression or Simple Average. If your complex LSTM can't beat a straight line, you have a problem.
*   **Challenger 1 (Gradient Boosting)**: XGBoost/LightGBM. Handles tabular data, missing values, and non-linearities exceptionally well. usually the winner for structured data.
*   **Challenger 2 (Deep Learning)**: LSTM/GRU/Transformer. Can learn temporal patterns (sequences) directly without manual rolling features.

## 2. Validation Strategy
*   **Random Split**: BANNED. If you randomly split, you will train on Tuesday and test on Monday. That's time travel.
*   **TimeSeriesSplit**: Train on Jan-Mar, Test on Apr. Then Train on Jan-Apr, Test on May.
*   **GroupKFold**: Ensure the same engine doesn't appear in both Train and Test. If the model memorizes "Engine #5's quirk", it won't generalize to "Engine #6".

## 3. Metrics
*   **RMSE**: Root Mean Square Error. (Standard).
*   **Early vs Late Penalty**: In maintenance, predicting failure *too late* is catastrophic. Predicting *too early* just wastes a mechanic's time. We often use a custom loss function that penalizes negatives (Late) 10x more than positives (Early).
