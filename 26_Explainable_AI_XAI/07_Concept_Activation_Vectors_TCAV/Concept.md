# TCAV (Testing with Concept Activation Vectors)

## 1. Pixel vs Concept
*   **Standard XAI**: "This pixel at (10, 20) is important." (Low Level).
*   **Human XAI**: "The stripes are important." (High Level).
*   **Problem**: The model input doesn't have a "Stripes" column. It only has pixels.

## 2. Defining a Concept
How do we teach the XAI tool what "Stripes" are?
1.  **Gather Examples**: Collect 50 images of striped textures (Zebras, Shirts, Barcodes).
2.  **Gather Negatives**: Collect 50 random images.
3.  **Train Probe**: Train a simple Linear Classifier on the internal activations (Latent Space) of the model to distinguish Stripes vs Random.
4.  **Concept Vector**: The vector orthogonal to the decision boundary is the "Stripe Direction" ($v_C$).

## 3. Testing Sensitivity
Now, for a Zebra image:
*   Calculate the directional derivative of the "Zebra" class score along the "Stripe Direction" vector.
*   If increasing "Stripiness" leads to higher "Zebra" probability, then the Concept is important.
