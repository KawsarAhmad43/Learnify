# Task: The Swiss Roll

## Objective
Unroll the Swiss Roll dataset.

## Data
`sklearn.datasets.make_swiss_roll(n_samples=1000)`

## Tasks
1.  **Generate Data**: Use `make_swiss_roll`. It returns 3D points ($X$) and their position on the roll ($t$).
2.  **PCA**: Reduce to 2D. Does it look like a squashed mess?
3.  **t-SNE**: Reduce to 2D. Can it "unroll" the paper strip into a rectangle?
