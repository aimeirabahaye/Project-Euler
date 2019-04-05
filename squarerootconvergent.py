#from math import sqrt
from fractions import Fraction as fraction
i = fraction(1,2)
count = 0
while count < 1000:
    print 1 + i, 1 + float(i)
    i = fraction(1, 2 + i)
    count += 1

