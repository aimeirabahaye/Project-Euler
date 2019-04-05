done = {}
max = 0
ans = 0
for n in xrange(1,1000000):
    count = 0
    x = n
    while x != 1:
        if x%2 == 0:
            x = x/2
        else:
            x = 3*x + 1
        try:
            count += done[x]
            break
        except KeyError:
            count += 1
    done[n] = count
    if count > max:
        max = count
        ans = n   

print ans