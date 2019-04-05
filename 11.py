from time import clock

def max_vertical_sum(lines):
    i = 0 #starting line
    max = 0
    while i < 17:
        column = 0
        a = lines[i].split(' ')
        b = lines[i+1].split(' ')
        c = lines[i+2].split(' ')
        d = lines[i+3].split(' ')
        while column < len(a):
            x = int(a[column])*int(b[column])*int(c[column])*int(d[column])
            if x > max:
                max = x
            column += 1
        i += 1
    return max
    
def max_pdiagonal_sum(lines):
    i = 0 #starting line
    max = 0
    while i < 17:
        column = 0
        a = lines[i].split(' ')
        b = lines[i+1].split(' ')
        c = lines[i+2].split(' ')
        d = lines[i+3].split(' ')
        while column <= 16:
            x = int(a[column])*int(b[column+1])*int(c[column+2])*int(d[column+3])
            if x > max:
                max = x
            column += 1
        i += 1
    return max
    
def max_sdiagonal_sum(lines):
    i = 0 #starting line
    max = 0
    while i < 17:
        column = 19
        a = lines[i].split(' ')
        b = lines[i+1].split(' ')
        c = lines[i+2].split(' ')
        d = lines[i+3].split(' ')
        while column >= 3:
            x = int(a[column])*int(b[column-1])*int(c[column-2])*int(d[column-3])
            if x > max:
                max = x
            column -= 1
        i += 1
    return max
        
def max_horizontal_sum(lines):
    i = 0 #starting line
    max = 0
    while i <= 19:
        column = 0
        a = lines[i].split(' ')
        while column < 17:
            x = int(a[column])*int(a[column+1])*int(a[column+2])*int(a[column+3])
            if x > max:
                max = x
            column += 1
        i += 1
    return max
lines = open('11.txt').readlines()
start = clock()
print max(max_vertical_sum(lines), max_sdiagonal_sum(lines), max_pdiagonal_sum(lines), max_horizontal_sum(lines))
print clock() - start