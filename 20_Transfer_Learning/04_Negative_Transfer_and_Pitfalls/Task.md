# Task: Domain Divergence

## Objective
Quantify similarity to decide on Transfer Learning.

## Domains
1.  **ImageNet**: Dogs, Cats, Cars, Fruits.
2.  **Satellite**: Roofs, Trees, Roads (Top-down view).
3.  **Microscope**: Cells, Bacteria (Transparent, blobs).

## Task
Rank the likelihood of Negative Transfer for a ResNet50 (ImageNet) applied to:
1.  **Cifar-10** (Low Negative Transfer risk).
2.  **Satellite Imagery**.
3.  **Microscope Imagery** (High Negative Transfer risk).

## Question
Why is the "Viewpoint" (Top-down vs Frontal) a major factor in Negative Transfer?
*   Answer: Features like \"legs\" or \"wheels\" basically disappear or look like rectangles in Satellite view. The filters looking for \"legs\" become noise generators.
