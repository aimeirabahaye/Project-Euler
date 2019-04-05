from time import clock

start = clock()
i = 1
found = False
while not found:
    x = set(str(i))
    y = set(str(i*2))
    z = set(str(i*3))
    l = set(str(i*4))
    k = set(str(i*5))
    h = set(str(i*6))
    if x == y == z == l == k == h:
        print i 
        found = True
    else:
        i += 1

print clock()
print clock()-start

