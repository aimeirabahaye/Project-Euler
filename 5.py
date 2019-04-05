def divisible(n):
    for x in range(11,21):
        if n%x != 0:
            return False
    return True
    
n = 20
while divisible(n) == False:
    n += 20

print n