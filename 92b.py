def square_digit_chains(n):
    if n == 1:
        return 1
    if n == 89:
        return 89
    str_n = str(n)
    next_n = 0
    for i in range(len(str_n)):
        next_n += int(str_n[i])**2
    return square_digit_chains(next_n)

done = {}    
for x in range(1,571):
    val = square_digit_chains(x)
    done[x] = val
count = 0    

for i in xrange(1,100):
    n = i
    str_n = str(n)
    next_n = 0
    for j in range(len(str_n)):
        next_n += int(str_n[j])**2
    n = next_n
    try:
        if done[n] == 89:
            count += 1
            done[i] = 89
    except KeyError:
        done[i] = square_digit_chains(i)
        if done[i] == 89:
            count += 1

print count
