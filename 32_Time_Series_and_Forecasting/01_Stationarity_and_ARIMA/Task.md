# Task: Seasonality

## Objective
Cycles.

## Setup
*   ARIMA handles Trends.
*   SARIMA handles Seasonality.
*   But what if you have MULTIPLE seasonalities? (Weekly cycle + Yearly cycle).
*   SARIMA struggles with this.

## Task
1.  **Prophet (by Meta)**: A decomposable additive model.
    *   $y(t) = g(t) + s(t) + h(t) + \epsilon(t)$.
    *   Trend + Seasonality + Holidays + Error.
2.  Prophet is robust to missing data and shifts (changepoints).
3.  **Task**: Install `prophet` and fit a model that accounts for the \"Christmas Spike\".

## Question
What is 'Exogenous Variable'?
*   Answer: External info. Predicting Ice Cream sales based on Past Sales (Univariate) vs Predicting sales based on Past Sales + Temperature (Exogenous). ARIMAX supports this.
