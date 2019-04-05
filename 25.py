a, b = 1, 2
list = [1,1,2]
while len(str(b)) < 1000:
 a, b = b, a + b
 list.append(b)
print len(list)