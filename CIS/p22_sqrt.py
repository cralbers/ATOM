'''
CIS 210 Project 2-2: Approximate Square Root

Author: Cora Albers

Credits: N/A

Use the Babylonian method to estimate the square root of a number
and compare its result to that of the math module function sqrt.
'''

import math

def main():
    '''Square root comparison program driver.'''
    sqrt_compare(25, 5)
    sqrt_compare(25, 10)
    sqrt_compare(625, 5)
    sqrt_compare(625, 10)
    sqrt_compare(10000, 8)
    sqrt_compare(10000, 10)
    sqrt_compare(10000, 11)
    return None

main()

def mysqrt(n, k):
    '''(int, int) -> float

    Calculates the square root of a number n
    using the Babylonian method with k number of iterations.

    >>> mysqrt(25, 5)
    5.000023178253949

    >>> mysqrt(49, 5)
    7.001406475243939
    '''

    x = 1
    for i in range(k):
        x = .5 * (x + n/x)

    return x

def sqrt_compare(num, iterations):
    '''(int, int) -> float

    Calculates the percentage error of the square root of number
    between the Babylonian method with the input number of iterations
    and the math function's sqrt method.

    >>> sqrt_compare(10000, 8)
    For 10000 using 8 iterations:
    mysqrt value is: 101.20218365353946
    math lib sqrt value is: 100.0
    This is a 1.2 percent error.

    >>> sqrt_compare(25, 5)
    For 25 using 5 iterations:
    mysqrt value is: 5.000023178253949
    math lib sqrt value is: 5.0
    This is a 0.0 percent error.
    '''

    sqrt1 = mysqrt(num, iterations)
    sqrt2 = math.sqrt(num)

    result = ((abs(sqrt2 - sqrt1))/sqrt2)*100

    result = round(result, 2)

    print("For " + str(num) + ' using ' + str(iterations) + ' iterations:')
    print('mysqrt value is: ' + str(sqrt1))
    print('math lib sqrt value is: ' + str(sqrt2))
    print('This is a ' + str(result) + ' percent error.')

    return None
