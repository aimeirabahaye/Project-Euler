from time import clock
from _utilities import prime

def sieve(numbers):
    i = 0
    while i < len(numbers):
        for x in numbers[i+1:]:
            if x%numbers[i]==0:
                numbers.remove(x)
                #print numbers
        i+=1
        if x > numbers[-1]**0.5:
            return numbers
                #return sieve(numbers)
            
            

start1 = clock()
numbers = range(2,1000000)
y = sieve(numbers)
print clock() - start1

start2 = clock()
primes = [i for i in range(2,100000) if prime(i) == True]
#print primes
print clock() - start2