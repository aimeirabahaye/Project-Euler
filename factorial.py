from operator import mul

def factorial(n):
    list = []
    if n == 0:
        return 1
    while n > 0:
        list.append(n)
        n -= 1
        product = reduce(mul,list, 1)
    return product
    
print factorial(41)