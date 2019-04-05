from time import clock

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
start = clock()
count = 0
done = {} 
for x in range(1,571):
    val = square_digit_chains(x)
    done[x] = val
terms = []
for i in xrange(1,10000):
    n = i
    while n != 1 and n != 89:
        str_n = str(n)
        next_n = 0
        for digit in range(len(str_n)):
            next_n += int(str_n[digit])**2
        terms.append(next_n)
        n = next_n
        try:
            if done[n] == 89:
                count += 1
                break
            elif done[n] == 1:
                break
        except KeyError:
            pass
    done[i] = n
    for number in terms[:-1]:
        done[number] = n

end = clock()
print count
print end - start