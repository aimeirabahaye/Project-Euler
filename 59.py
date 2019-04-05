from collections import Counter
file = [(int(n)) for n in open('59.txt').read().split(',')]
cryptedB = [format(n, 'b') for n in file]
for g in range(len(cryptedB)):
    zeroes = '0'
    zeroes_2_add = 7 - len(cryptedB[g])
    cryptedB[g] = zeroes * zeroes_2_add + cryptedB[g]

max_value = [71, 79, 68] #from counter

max_value_bin = [bin(i)[2:] for i in max_value]

def XOR_(string, k):
    string = str(string)
    key = ''
    for i in range(len(string)):
        b = int(string[i]) ^ int(k[i])
        key += str(b)
    return key #change to uncrypted string


def XOR(string):
    string = str(string)
    space = '0100000'
    key = ''
    for i in range(len(string)):
        b = int(string[i]) ^ int(space[i])
        key += str(b)
    return key

k1 = XOR(max_value_bin[0])
k2 = XOR(max_value_bin[1])
k3 = XOR(max_value_bin[2]) 

for i in range(0,len(cryptedB),3):
    cryptedB[i] = XOR_(cryptedB[i], k1)   
for i in range(1,len(cryptedB),3):
    cryptedB[i] = XOR_(cryptedB[i], k2)   
for i in range(2,len(cryptedB),3):
    cryptedB[i] = XOR_(cryptedB[i], k3)       

uncryptedB = [int(a, 2) for a in cryptedB]
ascii = ''.join([chr(a) for a in uncryptedB])
print ascii
print sum(uncryptedB)