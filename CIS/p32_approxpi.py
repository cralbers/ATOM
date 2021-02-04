'''
CIS 210 Project 3-2: Monte Pi (Approximating pi)

Author: Cora Albers

Credits: Based on code on p.78 Miller and Ranum text.

Approximate pi using a Monte Carlo simulation.
'''

import math
import random
import turtle
from turtle import *


def isInCircle(x, y, r):
    '''(int, int, int) -> bool

    Takes in x and y values to define the location of a point
    and then determines if the point lies within a inCircle
    or radius, r.

    >>> isInCircle(0, 0, 1)
    True
    >>> isInCircle(.5, .5, 1)
    True
    >>> isInCircle(1, 2, 1)
    False
    '''
    distance = math.sqrt(x**2 + y**2)

    if distance < r:
        return True
    else:
        return False


def montePi(numDarts):
    '''(int) -> float

    Takes in a value, numDarts, as the number of darts to call
    isInCircle on. For that number numDarts, creates random points
    calls isInCircle on each. Then approiximates the value of pi
    based on the number of darts that were in a circle of radius 1.

    >>> montePi(100)
    3.04
    >>> montePi(1)
    4.0
    >>> montePi(10000)
    3.11

    *due to randomness in generating points, the approximate value of
    pi that is returned will vary when the same number of darts is input*
    '''
    inCircle = 0

    for i in range(numDarts):
        x = random.random()
        y = random.random()

        isInCircle(x, y, 1)

        if isInCircle(x, y, 1):
            inCircle = inCircle + 1
        else:
            pass


    approxPi = inCircle/numDarts * 4
    return approxPi



def reportPi(numDarts, approxPi):
    '''(int, int) -> None

    Takes in a number of darts, numDarts and an approximate value of pi,
    approxPi, to determine the percent error of the approximate value
    from the math lib value.


    >>> reportPi(100, 3.2)
    With 100 iterations:
    My approximate value for pi is: 3.2
    The math lib pi value is 3.141592653589793
    This is a 1.86 percent error.

    >>> reportPi(100000, 3.14676)
    With 100000 iterations:
    My approximate value for pi is: 3.14676
    The math lib pi value is 3.141592653589793
    This is a 0.16 percent error.

    >>> reportPi(10000000, 3.141242)
    With 10000000 iterations:
    My approximate value for pi is: 3.141242
    The math lib pi value is 3.141592653589793
    This is a 0.01 percent error.
    '''
    pi1 = approxPi
    pi2 = math.pi

    result = ((abs(pi2 - pi1)) / pi2) * 100

    result = round(result, 2)

    print('With ' + str(numDarts) + ' iterations:')
    print('My approximate value for pi is: ' + str(pi1))
    print('The math lib pi value is ' + str(math.pi))
    print('This is a ' + str(result) + ' percent error.')

    return None

def main():
    '''(n/a) -> None

    Runs the reportPi function for 3 different values.

    >>> reportPi(100, 3.2)
    With 100 iterations:
    My approximate value for pi is: 3.2
    The math lib pi value is 3.141592653589793
    This is a 1.86 percent error.

    >>> reportPi(100000, 3.14676)
    With 100000 iterations:
    My approximate value for pi is: 3.14676
    The math lib pi value is 3.141592653589793
    This is a 0.16 percent error.

    >>> reportPi(10000000, 3.141242)
    With 10000000 iterations:
    My approximate value for pi is: 3.141242
    The math lib pi value is 3.141592653589793
    This is a 0.01 percent error.
    '''

    pi1 = montePi(100)
    reportPi(100, pi1)

    pi2 = montePi(100000)
    reportPi(100000, pi2)

    pi3 = montePi(10000000)
    reportPi(10000000, pi3)

    return None

main()
