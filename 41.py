import itertools

def prime(n):
 base = 2
 while base < n**0.5 + 1:
  if n%base == 0:
   return False
  if n%base !=0:
   base += 1
 return True

i = 0
x = '12'
next = 3
pandigital_prime = []
while len(x) < 9:
 perms = [''.join(i) for i in itertools.permutations(x)]
 for y in perms:
  if prime(int(y)) == True:
   pandigital_prime.append(y)
 x += str(next)
 next += 1

print max(pandigital_prime)
 