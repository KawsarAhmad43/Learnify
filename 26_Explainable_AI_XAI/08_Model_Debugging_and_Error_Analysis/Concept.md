# Model Debugging and Error Analysis

## 1. Aggregate Metrics are Lies
"98% Accuracy" sounds great.
But if the 2% failure rate is purely "Ambulances", your Self-Driving Car is a disaster.
You must look at **Slices**.

## 2. Slice Analysis
Break down performance by subgroups:
*   By Time: Day vs Night.
*   By Condition: Rainy vs Sunny.
*   By Complexity: Highway vs City.
*   **Result**: 
    *   Highway Day: 99.9%.
    *   Highway Night: 99.0%.
    *   City Rain: 30.0%. (Found the bug!)

## 3. Confusion Matrix
A grid showing "Predicted vs Actual".
*   Useful for multi-class.
*   Shows specific confusions: "It confuses Wolves for Huskies, but never Wolves for Cards".

## 4. Top-k Losses
Look at the examples where the Loss was HIGHEST.
These are the cases the model was *most wrong* about (Predicted 100% confidence "A", but it was "B").
Often reveals **Labeling Errors** (Human annotated it wrong).
