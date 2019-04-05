a = 2
sum_ = 0
while a < 200000:
    y = str(a)
    sum = 0
    for i in range(len(y)):
        sum += int(y[i])**5
        if sum == int(y):
            sum_ += a
        a += 1
print sum_