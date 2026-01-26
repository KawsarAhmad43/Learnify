# Project Scope: Predictive Maintenance System

## Objective
Build a production-ready ML pipeline to predict engine failure windows.

## Deliverables
1.  **Data Ingestion Pipeline**: Script to load, validate, and clean sensor streams.
2.  **Feature Store**: Logic to compute rolling signals (Mean, Std, Peak-to-Peak) over time windows.
3.  **Model Registry**: Trained XGBoost and LSTM models with versioning.
4.  **Inference Service**: Mock API that accepts sensor readings and returns `RUL` + `Risk_Level`.
5.  **Dashboard**: Streamlit app visualizing the degradation curve.

## Tools & Tech Stack
*   **Pandas/Polars**: Data Manipulation.
*   **Pandera**: Data Validation (Schema Enforcement).
*   **Scikit-Learn**: Preprocessing & metrics.
*   **XGBoost**: Gradient Boosting (interpretable baseline).
*   **PyTorch (LSTM)**: Deep Learning (complex patterns).
*   **SHAP**: Explainability.
*   **Optuna**: Hyperparameter Tuning.

## Success Criteria
*   **RMSE**: < 15 cycles (days).
*   **Inference Time**: < 50ms per record.
*   **Zero Leakage**: Strict temporal separation.

## Note on "Professionalism"
Unlike academic tutorials, we will treat data as "Dirty until proven Clean". Every notebook will start with strict Schema Validation. We will use Logging instead of `print()`. We will use Type Hints.
