# Task: News Classification

## Objective
Classify headlines as 'Sports' or 'Tech'.

## Data
*   **X**: ["Team wins the game", "New iPhone released", "Player scores goal", "Software update available"]
*   **y**: ["Sports", "Tech", "Sports", "Tech"]

## Tasks
1.  **Train**: Build a pipeline with `CountVectorizer` and `MultinomialNB`.
2.  **Predict**: Classify "Apple wins huge market share". (Note: 'Apple' is tech, 'wins' is usually sports. See what it does).
