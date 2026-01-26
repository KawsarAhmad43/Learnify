# Data Pipeline and EDA

## 1. Professional Data Validation
*   **Garbage In, Garbage Out**: If your sensor sends `NaN` or `-999`, your model will crash or lie.
*   **Schema Validation**: We use libraries like **Pandera** or **Pydantic** to enforce rules:
    *   `Temperature` must be float between 0 and 500.
    *   `Timestamp` must be unique and monotonic.
    *   `Status` must be in {"OK", "WARNING", "CRITICAL"}.
*   **Fail Fast**: If validation fails, stop the pipeline immediately. Do not silently proceed.

## 2. Exploratory Data Analysis (EDA)
*   **Target Analysis**: What is the distribution of RUL? Is it uniform?
    *   *Problem*: We have much more healthy data (RUL > 100) than failure data (RUL < 10). This is Class Imbalance (even in regression).
*   **Sensor Correlations**: Which sensors move together? (Multicollinearity).
    *   Sensors often drift over time due to wear, even if the machine is fine. We need to distinguish **Sensor Drift** from **Failure drift**.

## 3. Data Leakage
*   **Future Peaking**: Using data from Time T+1 to predict T.
*   **Split Leakage**: Randomly splitting time series.
*   **Normalization Leakage**: Calculating Mean/Std on the *entire* dataset before splitting. You must fit the scaler ONLY on the Training set.
