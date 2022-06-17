import numpy as np

nums = np.arange(1,101)
n = 100
num2 = n*(n+1) / 2

print(num2**2- np.sum(nums**2) )