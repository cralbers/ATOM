'''
CIS 210 Project 2-3: Draw Flower

Author: Cora Albers

Credits: N/A

Use the turtle module to generate a drawing of a flower.
'''

from turtle import *

def main():
    '''
    '''
    drawFlower(25)

    return None

def drawPolygon(sideLength, numSides):
    '''(int, int) -> turtle

    For an input of side length and number of sides, functions
    will generate a flower with input side length and the input
    number of sides for number of petals.

    >>> drawPolygon(4, 20)
    will generate turtle drawing with 20 petals of 4 length

    >>> drawPolygon(5, 16)
    will generate turtle drawing with 16 petals of 5 length
    '''
    turnAngle = 360/numSides

    for i in range(numSides):
        fd(sideLength)
        right(turnAngle)


    return None


def drawFlower(numSquares):
    '''(int) -> turtle

    For an input of number of squares, will call the function drawPolygon
    that number of times after drawing a flower stem.

    >>> drawFlower(5)
    will generate turtle drawing with a stem and 5 petals

    >>> drawFlower(6)
    will generate turtle drawing with a stem and 6 petals
    '''
    penup()
    goto(0, -100)
    pendown()
    goto(0,0)

    turnAngle = 360/numSquares
    for i in range(numSquares):
        drawPolygon(4, 25)
        right(turnAngle)


    return None


main()

