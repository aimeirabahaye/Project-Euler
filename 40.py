list = range(1,1000001)
number = ''
i = 0
while i < len(list) :
    number += str(list[i])
    i += 1
        
print int(number[0]) * int(number[9]) * int(number[99]) * int(number[999]) * int(number[9999]) * int(number[99999]) * int(number[999999])
 
