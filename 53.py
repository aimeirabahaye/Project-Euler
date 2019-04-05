from itertools import product
from _utilities import combinatoric

count = 0
for n,r in product(range(1,101),range(1,101)):
    if r < n:
        if combinatoric(n,r) > 1000000:
            count += 1
print count
  

