import itertools

for a,b,c in itertools.product(range(1,1000),range(1,1000),range(1,1000)):
 if a< b< c:
  x = (c**2 - b**2)**0.5
  y = 1000 - b - c
  if x == y:
   print int(x*b*c)
   break
