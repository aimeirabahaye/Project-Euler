def palyndrome(n):
 x = str(n)
 if x == x[::-1]:
  return True
 else: 
  return False

sum = 0
for i in range(1,1000000):
 if palyndrome(i):
  binary = int(bin(i)[2:])
  if palyndrome(binary):
   sum += i
print sum 

