
def d(a):
 div = 1
 divisor = []
 while div < a:
  if a%div == 0:
   divisor.append(div)
   div += 1
  if a%div != 0:
   div +=1
 return sum(divisor)

sum_amicable = 0
a = 1
for a in range(1,10000):
 b = d(a)
 if a == d(b) and a != b:
  sum_amicable += a 
print sum_amicable
  
  
   
