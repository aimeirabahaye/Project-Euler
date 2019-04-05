from math import log
from time import clock
start = clock()
file = open('99.txt')
lines_ = file.readlines()

y = {}
for i in xrange(1000):
   [base,exposant] = lines_[i].split(',')
   value = int(exposant)*log(int(base))
   y[value] = i
   
print y.get(max(y)) + 1

end = clock()

print '%ss' %(end-start)