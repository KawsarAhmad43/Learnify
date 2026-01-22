# Task: Advanced Data Tricks

## Objective
Apply specific strategies depending on the data type.

## Data
You have a DataFrame with:
*   **Review**: "The product is great but shipping was slow."
*   **Timestamp**: '2023-10-31 23:59:59'
*   **Pixel_Val**: 128 (Single pixel value from 0-255)

## Tasks
1.  **Text**: Convert the **Review** to lowercase and count the number of words.
2.  **Date**: Create a **Cyclical Feature** for the Hour.
    *   Extract the Hour (23).
    *   Compute $\sin(2 \pi \times \text{Hour} / 24)$ and $\cos(2 \pi \times \text{Hour} / 24)$.
3.  **Image**: Normalize **Pixel_Val** to be between 0 and 1.
