def add(x, y):
    'Adds two integers and returns the sum'
    if isinstance(x, float) and isinstance(y, float):
        return x + y
    else:
        return x + y

def factorial1(n):
    'Function returning the factorial of any given real number n.'
    number = 1
    if n < 0:
        pass
    elif n == 0:
        return 1
    else:
        for i in range(1, n+1):
            number = number*i
        return number

def sinus(x, n):
    '''
    Calculating an approximation to the sine function
    using the taylor series of sin(x)
    '''
    sum = 0
    for i in range(0, n+1):

        sign = (-1)**i
        teller = x**(2*i + 1)
        nevner = factorial1(2*i +1)
        sum += sign*(teller)/(nevner)

    return sum

def divide(x,y):
    'Dividing two given real numbers x and y'
    return x/y

def exp(x,n):
    '''
    Calculating an approximation to the exponential function (e^x)
    using the taylor series of e^x
    '''
    sum2 = 0

    for i in range(0, n+1):
        sum2 += (x**i)/factorial1(i)

    return sum2
def multi(x,y):
    '''
    Multiplying two real numbers x and y
    '''
    mul = x*y
    return mul
