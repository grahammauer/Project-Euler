'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a^2 + b^2 = c^2 

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc.
'''

import numpy as np

a = 1
b = 2
c = 3

for C in range(c,1000):
    for B in np.arange(b,C):

        for A in np.arange(a,B):

            if (int(A + B + C) == 1000 and (A**2 + B**2 == C**2)):
                print(A,B,C)
                print(int(A*B*C))
                break

        if (int(A + B + C) == 1000 and (A**2 + B**2 == C**2)):
            break

    if (int(A + B + C) == 1000 and (A**2 + B**2 == C**2)):
            break

