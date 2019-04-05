number_str = open('8number.txt').read()
list = []
max = 0
for i in range(len(number_str)-13):
    x = int(number_str[i]) * int(number_str[i+1]) * int(number_str[i+2]) * int(number_str[i+3]) * int(number_str[i+4]) * int(number_str[i+5]) * int(number_str[i+6]) * int(number_str[i+7])* int(number_str[i+8]) * int(number_str[i+9]) * int(number_str[i+10]) * int(number_str[i+11]) * int(number_str[i+12])
    if x > max:
        max = x
print max