"""
ML learning models understand numbers not text

Machine learning models can’t process text directly, they need numbers.

One-hot encoding turns categorical variables into binary vectors without implying any order, making them model-friendly without misleading the algorithm.

What It Shows
Converts each category in the Color column into its binary column
Each row has a 1 in the column that matches its category
Zero assumption of order, pure categorical handling
"""

import pandas as pd

# Sample data
df = pd.DataFrame({
    'Color': ['Red', 'Blue', 'Green', 'Blue']
})

print("----DF----")
print(df)
# One-hot encoding
encoded = pd.get_dummies(df, columns=['Color'])
print("----ENCODED----")
print(encoded)