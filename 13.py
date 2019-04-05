number = open('13.txt')
lines = number.readlines()
sum = 0
for i in range(100):
 sum += int(lines[i])
x = str(sum)
print x[:10]