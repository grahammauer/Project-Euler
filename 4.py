import numpy as np

def is_palin(number):
    
    str_number = str(number)
    length = len(str_number)
    
    if (length % 2) == 0: 
        counter = 0
        for i in range(int(length / 2)):
            if int(str_number[i]) == int(str_number[-i-1]):
                counter += 1
        if counter == length / 2:
            return True
        else:
            return False
                 
    else:
        counter = 0
        for i in range(int((length - 1) / 2)):
            if int(str_number[i]) == int(str_number[-i-1]):
                counter += 1
        if counter == (length - 1) / 2:
            return True
        else:
            return False

array = np.array([])
for i in range(900,999):
    for j in range(900,999):
        array = np.append(array, i*j)
        
array = np.sort(array)

keep_going = True
count = 1
while keep_going == True:
    if is_palin(int(array[-count])) == True:
        keep_going = False
        print(array[-count])
        
    else:
        count += 1

