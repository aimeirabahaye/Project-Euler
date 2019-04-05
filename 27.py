from _utilities import prime
import itertools

dict = {}
prime_under_1000 = [2]
for i in range(3,1000):
    if prime(i) == True:
        prime_under_1000.append(i)
        prime_under_1000.append(-i)


def cons_prime(a,b):
    x = 0
    y = x**2 + a*x + b
    while prime(y) == True:
        y = x**2 + a*x + b
        x += 1
    return x-1



for a,b in itertools.product(range(-999,1000,2), prime_under_1000):
    dict[cons_prime(a,b)] = a*b
print dict.get(max(dict))
