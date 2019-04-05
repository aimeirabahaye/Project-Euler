sum_of_the_squares = 0
for i in range(1,101):
    sum_of_the_squares += i**2

square_of_the_sum = (100*101/2)**2

print abs(square_of_the_sum - sum_of_the_squares)
