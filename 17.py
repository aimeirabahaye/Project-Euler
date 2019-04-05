from time import clock
from _utilities import number_in_letters
start = clock()
answer = 0
for i in range(1,1001):
    answer += len(number_in_letters(i))


print answer
end = clock()
print '%ss' %(end-start)
