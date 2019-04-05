def factorial2(n):
    'Given a number "n" as its argument, this function returns the factorial of n (n!).'
    if n == 1 or n == 0:
        return 1
    else:
        return n*factorial(n-1)
        
def factorial(n):
    'Given a number "n" as its argument, this function returns the factorial of n (n!).'
    if n == 1 or n == 0:
        return 1
    else:
        fact = n
        for x in range(1,n):
            fact *= x
    return fact

def isPrime(n):
    'Given a number "n" as its argument, this function returns "True" if "n" is prime and "False" if "n" is not prime.'
    if n == 2:
        return True
    if n < 2:
        return False
    for base in xrange(2,int(n**0.5 + 1)):
        if n%base == 0:
            return False
    return True

def number_in_letters(n):
    numbers = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six',
    7:'seven', 8:'eight', 9:'nine', 10:'ten', 11:'eleven', 12:'twelve',
    13:'thirteen', 15:'fifteen', 18:'eighteen', 20:'twenty', 30:'thirty',
    40:'forty', 50:'fifty', 60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety',
    100:'onehundred', 200:'twohundred', 300:'threehundred', 400:'fourhundred',
    500:'fivehundred', 600: 'sixhundred', 700:'sevenhundred', 800:'eighthundred', 900:'ninehundred', 1000:'onethousand' }
    try:
        return numbers[n]
    except KeyError:
        x = str(n)
        y = int(x[-1])
        
        if n < 20:
            return number_in_letters(y) + 'teen'
        elif 20 < n < 30:
            return 'twenty' + number_in_letters(y)
        elif 30 < n < 40:
            return 'thirty' + number_in_letters(y)
        elif 40 < n < 50:
            return 'forty' + number_in_letters(y)
        elif 50 < n < 60:
            return 'fifty' + number_in_letters(y)
        elif 60 < n < 70:
            return 'sixty' + number_in_letters(y)
        elif 70 < n < 80:
            return 'seventy' + number_in_letters(y)
        elif 80 < n < 90:
            return 'eighty' + number_in_letters(y)
        elif 90 < n < 100:
            return 'ninety' + number_in_letters(y)
        elif len(x) == 3:
                c = int(x[0])
            if x[1] == '0':
                return number_in_letters(c) + 'hundredand' + number_in_letters(y)
            else:
                dig = int(x[1:])
                return number_in_letters(c) + 'hundredand' + number_in_letters(dig)
                
def combinatoric(r,n):
    return factorial(n)/(factorial(r)*factorial(n-r))

def primesUpTo(n):
    'Given a number "n" as its argument, this function returns all the prime number(s) up to "n" in a list.'
