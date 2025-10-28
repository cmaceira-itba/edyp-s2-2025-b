import numpy as np


a = np.arange(10)
b = np.arange(10)[::-1]

print(np.array_equal(a.sort(),b.sort()))
