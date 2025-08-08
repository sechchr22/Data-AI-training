"""
Why numpy vectors are faster than loops?
Vectorization in NumPy allows you to apply operations on whole arrays without writing manual loops.

It’s cleaner, faster, and ideal for handling large datasets.
Using optimized C code under the hood supercharges performance and is a must-know for every data scientist.
"""
import numpy as np
import time

size = 1_000_000
a = np.random.rand(size)
b = np.random.rand(size)

start = time.time()

# Traditional loop
result = []
for i in range(size):
    result.append(a[i] + b[i])
print("Loop Time:", round(time.time() - start, 4), "seconds")

# Vectorized operation
start = time.time()
result_vectorized = a + b
print("Vectorized Time:", round(time.time() - start, 4), "seconds")