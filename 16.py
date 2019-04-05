number = 2**1000
digits = str(number)
sum = int(digits[0])
for i in range(1,len(digits)):
    sum += int(digits[i]) 
print sum
