'''
CIS 210 Midterm

Author: Cora Albers

Credits: N/A

Description: Write a function to calculate the distance between an input
(x, y) point and the origin (0,0). Then write a function that prints whether or
not the input (x, y) point is within a given radius, r.
'''
from math import sqrt

def myDist(x, y):
    '''(int, int) -> float

    Calculates the distance between the origin (0, 0) and an input (x, y)
    point using the Euclidean distance formula.

    >>> myDist(1, 1)
    1.4142135623730951
    >>> myDist(1, 2)
    2.23606797749979
    >>> myDist(2, 2)
    2.8284271247461903
    '''
    distance = sqrt(x**2 + y**2)

    return distance

def isIn(x, y, r):
    '''(int) -> None

    Determines if the point (x, y) is within an input radius, r.

    >>> isIn(.5, .5, 1)
    The point (0.5, 0.5) is in the circle of radius 1.
    >>> isIn(1, 1, 1)
    The point (1, 1) is not in the circle of radius 1.
    >>> isIn(2, 2, 1)
    The point (2, 2) is not in the circle of radius 1.
    '''

    distance = myDist(x, y)

    if distance < r:
        print('The point (' + str(x) + ', ' + str(y) + ') is in the circle of radius ' + str(r) +'.')
    else:
        print('The point (' + str(x) + ', ' + str(y) + ') is not in the circle of radius ' + str(r) +'.')
