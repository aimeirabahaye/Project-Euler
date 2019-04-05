from time import clock
from fractions import Fraction as fraction
start = clock()
i = fraction(1,2)
count = 0
answer = 0
for x in range(1000):
    i = fraction(1, 2 + i)
    a,b = str(1 + i).split('/')
    if len(a) > len(b):
        answer += 1
end = clock()
print answer
print end - start
