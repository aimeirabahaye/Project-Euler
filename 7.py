from _utilities import prime
from time import clock

start = clock()

count = 1
i = 1
while count < 10001:
    if prime(i) == True:
        count += 1
    i += 2
    
print i
print clock() - start