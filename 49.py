from _utilities import prime
from time import clock
from itertools import permutations
list = []
start = clock()
for i in xrange(1001,9999,2):
    if prime(i) == True:
        list.append(i)


for x in list:
    x = str(x)
    count = 0
    perms = [('').join(i) for i in permutations(x)]
    candidates = []
    for y in set(perms):
        if int(y) != int(x) and int(y) in list:
            candidates.append(int(y))
        candidates = sorted(candidates)
    if len(candidates) == 3:
        if abs(int(candidates[2])-int(candidates[1])) == abs(int(candidates[1])-int(candidates[0])):
            print str(candidates[0]) + str(candidates[1]) + str(candidates[2])
            end = clock()
            print '%ss' %(end - start)     
            break

