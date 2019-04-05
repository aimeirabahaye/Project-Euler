from utilities import *
from time import *

def goldbach(n):
    prime_list = [2,3,5,7]
    a = 11
    while a < n:
        if prime(a) == True:
            prime_list.append(a)
        a += 2
    for a in prime_list:
        if int(a) < n:
            b = int(((n-int(a))/2)**0.5)
            if n == a + 2*b**2:
                return True
    return False

    
n = 11
start = clock()    
while True:
    if prime(n) == False and goldbach(n) == False:
        print n
        break
    n += 2
print clock()-start