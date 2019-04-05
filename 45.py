def make_hexagonal(n):
    return n*(2*n-1)
    
def make_triangular(n):
    return n*(n-1)/2
    
def make_pentagonal(i):
    return i*(3*i-1)/2

i = 285
hexagonals = []
triangulars = []
pentagonals = []
c = 0
while True:
    c = make_triangular(i)
    hexagonals.append(make_hexagonal(i))
    pentagonals.append(make_pentagonal(i))
    if c in hexagonals and c in pentagonals:
        print c
        break
    i += 1
    
