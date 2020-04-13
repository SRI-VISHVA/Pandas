import numpy as np
import pandas as pd

s1 = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s1)

s2 = pd.Series([1, 3, 5, 6, 8])
print(s2)

s3 = pd.Series([1, 3, 'three', 6, 8])
print(s3)

s4 = pd.Series([1, 3, 99., 6, 8])
print(s4)

s5 = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])
print(s5)

s6 = pd.Series(np.random.randn(5))
print(s6)

print(type(s5.index))

d = {'b': 1, 'a': 0, 'c': 2}
s7 = pd.Series(d)
print(s7)

e = pd.Series([5, 6, 7, 99, 100, 12, 234])
print(e)
print('-----------------------')
print(e.median)
print('***********************')
print(e[e > e.median()])
# x
print(np.exp(e))

print(e[[2, 3, 4]])

print('new-----')
print(s5)
print(s5.array)
print(np.array(s5))
print(s5.tail())
