from _utilities import prime

sum_ = 2
for i in range(1,15000,2):
    if prime(i) == True:
        print i
        sum_ += i 

print sum_