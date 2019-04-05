import itertools
count = 0
for a,b,c,d,e,f,g,h in itertools.product(range(201), range(101), range(41), range(21), range(11),range(5), range(3), range(2)):
 if a + b*2 + c*5 + d*10 + e*20 + 50*f + 100*g + 200*h == 200:
  count += 1
  print count
 