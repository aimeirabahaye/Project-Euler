from _utilities import *

def sum_factorial(n):
    string_number = str(n)
    sum = 0
    i = 0
    while i < len(string_number):
        if factorial(int(string_number[i])) > n:
            return False
        else:
            sum += factorial(int(string_number[i]))
        i += 1
    if sum == n:
        return True

answer = 0        
for x in range(3,40600):
    if sum_factorial(x) == True:
       answer += x
       
print answer