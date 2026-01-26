# Task: The "Cyan" Filter

## Objective
Remove the Red channel from an image to simulate a filter.

## Steps
1.  Load the `china.jpg` image again using `load_sample_image`.
2.  Make a **copy** of the image (so you don't modify the original).
3.  Set the entire Red channel (index 0) to 0.
4.  Visualize the result.

## Expectation
*   The image should look "Cyan" (Blue-Greenish), because Red is gone.
*   Cyan = Green + Blue.
