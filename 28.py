sum = 1 
limit = 1001*1001
u = 1
next = 2
count = 1
i = 3
u = 1 #nth 'squared' formed
while i <= limit:
    sum += i
    if count == 4:
        count = 0
        u += 1
        next = 2*u
    count += 1
    i+=next

print sum
    