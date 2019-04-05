from time import *
start = clock()
sum = 0
for i in range(1,1001):
 sum += i**i
x = str(sum)
print x[-10:]

y = str(clock()-start)
print '%ss' % y[:6]
