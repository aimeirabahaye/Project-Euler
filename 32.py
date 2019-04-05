from itertools import permutations
digits = ''
for i in range(1,10):
    digits += str(i)
    
list = [''.join(i) for i in permutations(digits)]

print len(list)
