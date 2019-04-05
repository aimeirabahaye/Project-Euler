from _utilities import prime
from time import clock

i = 646
b = 2
def number_of_prime_factors(n):
    factors = []
    number = 0
    for i in xrange(2,int(n**0.5)):
        if n%i == 0:
            factors.append(i)
            factors.append(n/i)
    for x in factors:
        if prime(x) == True:
            number += 1
    return number
start = clock()
for i in xrange(646,1000000):
    if number_of_prime_factors(i) == 4 and number_of_prime_factors(i+1) == 4 and number_of_prime_factors(i+2) == 4 and number_of_prime_factors(i+3) == 4:
        print i
        break
end = clock()

print end - start