import numpy as np

a = 1
b = 2

fib = np.array([1,2])

while (a + b) < 4000000:
    f = a + b
    a = b
    b = f
    fib = np.append(fib,f)
    
sum = 0
for i in range(len(fib)):
    
    if (fib[i]%2 == 0):
        sum += fib[i]
    
print(sum)