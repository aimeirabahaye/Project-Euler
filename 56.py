import itertools
list =[]
for a,b in itertools.product(range(1,100),range(1,100)):
 x = a**b
 digits = str(x)
 sum = int(digits[0])
 for i in range(1,len(digits)):
  sum += int(digits[i]) 
  list.append(sum)
print max(list)