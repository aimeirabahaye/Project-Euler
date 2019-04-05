from operator import mul
n = 100

list = []
sum = 0
while n > 0:
 n -= 1
 if n != 0:
  list.append(n)
product = reduce(mul,list, 1)
str_prod = str(product)
for i in range(len(str_prod)):
 sum += int(str_prod[i])
print sum