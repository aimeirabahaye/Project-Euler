import string
from time import clock
def coded_triangle(n):
    i = 0
    sum_str = 0
    next = 1
    while i < len(n):
        x = n[i].lower()
        y = string.lowercase.index(x) + 1
        sum_str += y
        i += 1
    while sum(range(next)) <= sum_str:
        if sum(range(next)) == sum_str:
            return True
        next += 1
    return False
start = clock()    
file = open('42.txt').read()

names = file.split('","')

o = names[0]
u = names[-1]
names[0] = o[1:]
names[-1] = u[:-1]
i = 0
answer = 0
while i < len(names):
    if coded_triangle(names[i]) == True:
        answer += 1
    i += 1
print answer
print clock() - start

