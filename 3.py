from _utilities import prime
number = 600851475143
list =[]
prime_multiple = []
for i in range(3,int(number**0.5),2):
    if number%i == 0:
        list.append(i)

for y in list:
 if prime(y) == True and y != 1:
  prime_multiple.append(y)
print prime_multiple[-1]
