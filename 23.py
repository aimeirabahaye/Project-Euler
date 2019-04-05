from itertools import product

def abundant(n):
    properdivisors = 1
    for b in range(2, int(n**0.5) + 1):
        if n%b == 0:
            properdivisors += b
            if n/b != b:
                properdivisors += n/b
    if properdivisors > n:
        return True
    
abundant_numbers = [i for i in range(1,28124) if abundant(i)]

sumofabundant = [] 
for a in abundant_numbers:
    for b in abundant_numbers:
        x = a + b
        if x > 28123:
            break
        else:
            sumofabundant.append(x)
         
sumofab = set(sumofabundant)
print  28123*28124/2 - sum(sumofab)