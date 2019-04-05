p = 840
count = 0
for a in range(1,p):
 for b in range(1,p-a):
  if a < b:
   if p - a - b == (a**2 + b**2)**0.5:
    count += 1
print count
 
