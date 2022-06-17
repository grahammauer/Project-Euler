sum = 0
i=1
while i < 1000:
    
    if (i%3 == 0) and (i%5 == 0):
        sum += i
    
    if (i%3 == 0) and (i%5 != 0):
        sum += i
        
    if (i%3 != 0) and (i%5 == 0):
        sum += i
    i+=1 
print(sum)