import math
import doctest

def circle_area(diameter):
    '''(int) -> float

    Calculates the area of a circle given the diameter.

    >>> circle_area(5)
    19.6349

    >>> circle_area(10)
    78.5398
    
    '''
    radius = diameter / 2
    area = math.pi * radius**2

    return area
  
    
def pizza_calculator(diameter, cost):
    '''
    (int, num) -> float
    Calculates and returns the cost per square inch
    of pizza for a pizza of given diameter and cost.
    Examples:
    >>> pizza_calculator(14, 18)
    0.117
    >>> pizza_calculator(14, 20.25)
    0.132
    '''
    area = circle_area(diameter)
    cost_per_inch = cost / area
    cost_per_inch = round(cost_per_inch, 3)
    return cost_per_inch


print(doctest.testmod())


