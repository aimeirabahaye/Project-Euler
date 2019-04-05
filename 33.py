from itertools import product
numerator = []
denominator = []
def digit_canceling(a,b):
    fraction = float(a)/b
    str_a = str(a)
    str_b = str(b)
    if a%10 == 0 and b%10 == 0 or a==b:
        return False
    else:
        for i in str_a:
            if i in str_b:
                x = i
        a_canceled = str_a.replace(i,'')        
        b_canceled = str_b.replace(i,'')
        if a_canceled == '':
            a_canceled = str_a[0]
        if b_canceled == '':
            b_canceled = str_b[0]
        if b_canceled == '0':
            return False
        
        if float(int(a_canceled))/int(b_canceled) == fraction:
            denominator.append(int(b_canceled))
            numerator.append(int(a_canceled))
            return True
    return False

for x,y in product(range(11,100),range(12,100)):
        if float(x)/y > 1:
            pass
        if digit_canceling(x,y) == True:
            r = 2
u= denominator[0]*denominator[1]*denominator[2]*denominator[3]
i= numerator[0]*numerator[1]*numerator[2]*numerator[3]

print '%s/%s' %(u,i), u/i 


