import string
from time import *

def score(n):
    i = 0
    sum_str = 0
    next = 1
    while i < len(n):
        x = n[i].lower()
        y = string.lowercase.index(x) + 1
        sum_str += y
        i += 1
    return sum_str

start = clock()    
file = open('22.txt').read()
unsorted = file.split('","')
x = unsorted[0]
y = unsorted[-1]
unsorted[0] = x[1:]
unsorted[-1] = y[:-1]
sorted = sorted(unsorted)

i = 0
answer = 0
while i < len(sorted):
    y = i + 1
    answer += y * score(sorted[i])
    i += 1
print answer
time = str((clock()-start))
print time[:6]
    
    
