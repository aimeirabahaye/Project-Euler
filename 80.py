def squarerootapprox(n, prec):
    a = 5*n
    b = 5
    while len(str(b)) < prec:
        if a >= b:
            a -= b
            b += 10
        else:
            a = int(str(a) + "00")
            b = int(str(b)[:-1] + "05")
    return b
         
def sumdigits(n):
    sumdigits = 0
    n = str(n)[:101]
    for dig in n:
        sumdigits += int(dig)
    return sumdigits
    
numbers = range(1,101)
for i in range(1,11):
    numbers.remove(i*i)
ans = 0
for num in numbers:
    n = squarerootapprox(num, 102)
    x = sumdigits(n)
    ans += x


n = input()
prec = input()
    
print squarerootapprox(n, prec)
        