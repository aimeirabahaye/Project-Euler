textFile = open("79.txt", 'r').readlines()

NUMBERS_OF_ATTEMPTS = 50
attempts = []

for i in range(NUMBERS_OF_ATTEMPTS):
    attempts.append(textFile[i][:3])

class Num(object):
    def __init__(self):
        self.left = []
        self.right = []

dic = {}

for i in range(10):
    dic[str(i)] = Num()

for attempt in attempts:
    dic[attempt[0]].right.append(attempt[1])
    dic[attempt[0]].right.append(attempt[2]) 

    dic[attempt[1]].right.append(attempt[2]) 
    dic[attempt[1]].left.append(attempt[0]) 

    dic[attempt[2]].left.append(attempt[0]) 
    dic[attempt[2]].left.append(attempt[1])

for n, keys in enumerate(dic):
   lst = dic[keys].right
   print n, lst

    