import numpy as np

keep_going = True

number = 1
maxfactor = 1

while (keep_going == True and number < 1e9):
    subcount = 0
    for i in range(11,20):
        if  (20 * number) % i == 0:
            subcount += 1
            
    if subcount == 10:
        print(number * 20)
        keep_going = False
    
    if subcount > maxfactor:
        maxfactor = subcount
        print(maxfactor, number*20)
    
    else:
        number += 1