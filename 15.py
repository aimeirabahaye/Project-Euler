from _utilities import factorial
from time import clock

def combinatoric(r,n):
    return factorial(n)/(factorial(r)*factorial(n-r))

start = clock()  
print combinatoric(20,40)
end = clock()
print abs(start - end)