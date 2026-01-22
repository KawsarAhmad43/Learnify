# Feature Engineering Techniques

## 1. What is Feature Engineering?
Feature Engineering is the art of creating new features from existing data to better represent the underlying problem to the predictive models. "Better features often beat better algorithms."

## 2. Common Techniques

### Polynomial Features
Generating interaction terms and powers of simple features.
*   If we have feature $x$, we add $x^2, x^3$.
*   If we have $x, y$, we add $xy, x^2, y^2$.
*   **Why?**: Allows linear models to fit non-linear data.

### Interaction Terms
Specifically multiplying two features together.
*   Example: `Area = Width * Height`. The model might not learn this relationship easily if only given Width and Height separately.

### Binning (Discretization)
Converting continuous variables into categorical bins.
*   Example: Age -> [0-18, 19-35, 36-60, 60+].
*   **Why?**: Can handle outliers and non-linear relationships.

### Log and Power Transformations
*   **Log Transform**: $\log(x+1)$. Compresses the range of high-skew distributions (like income or population). Makes residuals more normal.
*   **Box-Cox**: A family of power transformations to stabilize variance and make data more normal.

## 3. Domain-Specific Engineering
*   **Date/Time**: Extract Day of Week, Month, Is_Holiday, Hour of Day.
*   **Text length**: Count of words, characters.
