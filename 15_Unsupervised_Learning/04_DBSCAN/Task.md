# Task: Concentric Circles

## Objective
Cluster a "Donut" shape dataset.

## Data
`sklearn.datasets.make_circles(factor=0.5, noise=0.05)`

## Tasks
1.  **Generate Data**: Use the function above.
2.  **Try K-Means**: Show that it cuts the donut in half (imperfectly).
3.  **Use DBSCAN**: Tune `eps` until you capture the inner ring and outer ring as 2 separate clusters.
