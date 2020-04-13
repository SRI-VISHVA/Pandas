import numpy as np
import pandas as pd

# s = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
s = pd.Series([1, 2, 3, 4, 5])
s2 = pd.Series([6, 7, 8, 9, 10])

# Checking if an index exists
print('d' in s)

# Checking the data type of index in a Series
print(s.index.dtype)
print(np.dtype(s.index))

# Checking the data type of value in a Series
# print(np.dtype(s['a']))
print(np.dtype(s.get('a')))

print('-'*15)
# Adding two Series
print(s + s2)
