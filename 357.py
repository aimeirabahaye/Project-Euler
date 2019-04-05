from _utilities import isPrime 

def generatingPrime(n):
    for num in range(1,int(n**0.5) + 1):
        if n%num == 0:
            divisor1 = num
            divisor2 = n/num
            generatedPrime1 = divisor1 + n/divisor1
            generatedPrime2 = divisor2 + n/divisor2
            if not (isPrime(generatedPrime1) and isPrime(generatedPrime2)):
                return False
    return True 

sum = 1              
for i in xrange(0,100000000,2):
    if generatingPrime(i):
        print i
        print "YES"