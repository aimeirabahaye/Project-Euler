import itertools
list = []
for a,b in itertools.product(range(2,101), range(2,101)):
  x = a**b
  list.append(x)
y = set(list)
print len(y)