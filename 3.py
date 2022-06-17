import numpy as np

number = 600851475143

def SieveOfEratosthenes(n):

    prime = np.array([True for i in range(n + 1)])
    p = 2
    
    while (p * p <= n):
          
        if (prime[p] == True):
            
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1
    prime[0]= False
    prime[1]= False
    
    values = np.array([])
    for i in range(len(prime)):
        if prime[i] == True:
            values = np.append(values, int(i))
            
    return values
    
possible_factors = SieveOfEratosthenes(int(number**(1/2)))

factors = np.array([])
for i in range(len(possible_factors)):
    if (number % possible_factors[i] == 0):
        factors = np.append(factors, possible_factors[i])
        
print(np.max(factors))

