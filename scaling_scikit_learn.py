"""
Why is it so important?

Feature scaling is the backbone of good model performance. Without it, algorithms like KNN, SVM, or Gradient Descent-based models can give poor or biased results.
It ensures all features contribute equally, especially when they’re on different scales.

Not scaling your features can make even the best model perform worse than a basic one. Tiny preprocessing = huge difference in accuracy!
"""

"""
What happens here:
    fit_transform(X):

    fit: Calculates the mean and standard deviation for each feature (column).

    transform: Applies the transformation: $$ z = \frac{x - \mu}{\sigma} $$ Where:

    𝑥
    is the original value

    𝜇
    is the mean of the feature

    𝜎
    is the standard deviation

    The result is a new array scaled_X where:

    Each feature has mean = 0 and standard deviation = 1

    This is useful for many machine learning algorithms that are sensitive to feature scales (e.g., SVM, KNN, gradient descent-based models)
"""
from sklearn.preprocessing import StandardScaler
import numpy as np

# Sample data: [height (cm), weight (kg)]
X = np.array([[170, 65], [180, 85], [160, 55]])

scaler = StandardScaler()
scaled_X = scaler.fit_transform(X)

print(scaled_X)