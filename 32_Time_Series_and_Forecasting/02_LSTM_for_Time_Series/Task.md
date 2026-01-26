# Task: Multivariate Forecasting

## Objective
More than one variable.

## Setup
*   **Univariate**: Input = [Price], Output = [Price].
*   **Multivariate**: Input = [Price, Volume, TwitterSentiment], Output = [Price].

## Task
1.  Adjust the Input Size of your LSTM from 1 to 3.
2.  **Lookahead Bias**: Be careful! You cannot use *tomorrow's* Twitter Sentiment to predict *tomorrow's* price (because you don't know it yet). You can only use *yesterday's* sentiment.
3.  **Task**: Train a multivariate LSTM to predict `sine(t)` using `sine(t-1)` and `cosine(t-1)`.

## Question
What is 'Seq2Seq'?
*   Answer: Encoder-Decoder architecture. Input 10 days -> Output 5 days. (Forecasting multiple steps into the future at once). Better than recursive prediction (predict 1 day, feed it back, predict next day) because errors don't accumulate as fast.
