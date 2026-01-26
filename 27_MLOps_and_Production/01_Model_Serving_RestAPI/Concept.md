# Model Serving (REST API)

## 1. The Gap
*   **Data Scientist**: "Here is the `.ipynb` file."
*   **Engineering**: "I can't run a Jupyter notebook in the iPhone app."
*   **Solution**: Wrap the model in an API (Application Programming Interface).

## 2. Fast API / Flask
Lightweight Python web frameworks.
*   **Endpoint**: A URL (e.g., `/predict`).
*   **Request**: JSON input (`{"age": 30, "salary": 50000}`).
*   **Response**: JSON output (`{"approved": true}`).

## 3. Serialization
How to save the "Brain"?
*   **Pickle**: Python-specific. Easy but unsafe (can run arbitrary code).
*   **ONNX (Open Neural Network Media)**: Universal format. Train in PyTorch, run in C++, JavaScript, or Java. Optimized for speed.

## 4. Batch vs Realtime
*   **Realtime**: Single request, <100ms latency. (FastAPI).
*   **Batch**: Process 1 Million records overnight. (Airflow / Spark).
