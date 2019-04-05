def palyndrome(n):
 x = str(n)
 if x == x[::-1]:
  return True
 else: 
  return False
 
def lychrel(n):
 count = 1
 while count <= 50:
  x = str(n)
  reverse_ = x[::-1]
  a = int(reverse_) + n
  if palyndrome(a) == True:
   return False
  else:
   n = a
  count += 1
 return True
  

number = 0
for n in range(1,10000):
 if lychrel(n) == True:
  number += 1
print number