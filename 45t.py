from sets import *
from time import *
def make_hexagonal(n):
    return n*(2*n-1)
    
def make_pentagonal(i):
    return i*(3*i-1)/2

start = clock()
hexagonals = set([make_hexagonal(i) for i in range(286,100000)])
pentagonals = set([make_pentagonal(i) for i in range(286,100000)])

x = list(hexagonals.intersection(pentagonals))
print str(x[0])

print '%ss' % (clock()-start)



    
