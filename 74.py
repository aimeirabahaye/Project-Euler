def factorial(n):
    if n == 0:
        return 1

    val = n
    for i in range(1,n):
        val *= i
    
    return val 

def next(n):
    digits = [int(a) for a in str(n)]
    val = 0

    for digit in digits:
        val += factorial(digit)

    return val

def sortedDigitsNumber(n):
    return int("".join(sorted(str(n))))

def digitFactorialChain(n, cache):
    startingNumber = sortedDigitsNumber(n)
    currentNumber = sortedDigitsNumber(n)
    visited = {currentNumber : True}
    count = 1
    continueChecking = True
    while continueChecking:
        currentNumber = sortedDigitsNumber(next(currentNumber))
        visited[currentNumber] = True
        if cache.get(currentNumber, False):
            count += cache[currentNumber]
            continueChecking = False

        elif visited.get(currentNumber, False):
            continueChecking = False
        
        else:
            count += 1

    cache[startingNumber] = count  
    return count

cache = {}
count = 0
for i in xrange(1,1000000000):
    if digitFactorialChain(i, cache) == 60:
        count += 1

print count



