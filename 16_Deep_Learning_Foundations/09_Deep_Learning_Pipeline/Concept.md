# Deep Learning Pipeline

## 1. The 5-Step Pipeline
Professional Deep Learning code always follows this structure, regardless of the library (PyTorch, TensorFlow, JAX).

### Step 1: Data (ETL)
*   **Extract**: Load images/text.
*   **Transform**: Normalize (0-1), Resize, Augment.
*   **Load**: Batch the data (e.g., 32 images at a time).

### Step 2: Architecture (Model)
*   Define the structure (inputs $\to$ hidden $\to$ outputs).

### Step 3: Configuration (Loss & Optimizer)
*   **Loss**: How wrong is it? (CrossEntropy).
*   **Optimizer**: How to fix it? (Adam).

### Step 4: The Training Loop
*   For each Batch:
    1.  **Forward**: Predict.
    2.  **Loss**: Measure error.
    3.  **Backward**: Calculate gradients.
    4.  **Step**: Update weights.
    5.  **Zero Grad**: Clear gradients for next step.

### Step 5: Evaluation
*   Turn off gradients (no training).
*   Measure accuracy on unseen data.

## 2. Why Class-Based?
Instead of spaghetti code, we wrap the Trainer in a class.
*   **Encapsulation**: Keeps state (current epoch, best accuracy) safe.
*   **Reusability**: Use the same Trainer for different models.
