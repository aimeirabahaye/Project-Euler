from _utilities import prime
from time import clock

def rotation(number):
    number = str(number)
    str_number = str(number)
    rotated = ''
    rotations = []
    while rotated != number:
        rotated = str_number[1:]+str_number[0]
        str_number = rotated
        rotations.append(str_number)
    return rotations

def circular_prime(number):
    if prime(number) == False:
        return False
    number = str(number)
    str_number = str(number)
    rotated = ''
    while rotated != number:
        rotated = str_number[1:]+str_number[0]
        str_number = rotated
        if prime(int(rotated)) == False:
            return False
    return True
start = clock() 
count =  1
for i in xrange(1,1000000,2):
    if circular_prime(i) == True:
        count += 1
        
print count
print clock() - start    
