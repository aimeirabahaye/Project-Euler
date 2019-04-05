from _utilities import isPrime 

def d1(n):
    return 1 + 4*n**2 

def d2(n):
    return 1 + 4*n**2 - 2*n 

def d3(n):
    return (2*n + 1)**2 

def d4(n):
    return (2*n + 1)**2 - 2*n
    
def countNumInDiagonal(n):
    return 4*n + 1

countOfPrimes = 0
ratio = 100
n = 1 
while ratio > 0.1:
    if isPrime(d1(n)):
        countOfPrimes += 1
        
    if isPrime(d2(n)):
        countOfPrimes += 1
        
    if isPrime(d4(n)):
        countOfPrimes += 1
        
    ratio = float(countOfPrimes)/countNumInDiagonal(n)
    n += 1

print d3(n-1)**0.5 

