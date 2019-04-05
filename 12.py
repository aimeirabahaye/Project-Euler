def divisors(n):
    list = []
    for i in range(1,int(n**0.5)):
        if n%i == 0:
            list.append(i)
            list.append(n/i)
    return len(list)


x = 7
while divisors(sum(range(x))) < 500:
    x += 1

print sum(range(x))