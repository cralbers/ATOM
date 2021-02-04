'''
Project 1-2: Python Variations
CIS 210 Project 1-2

Author: Cora Albers

Credits: N/A

Basic number manipulation exercises.
'''
def convert (i,j,k):
    '''(num, num, num) -> str

    Takes in variables i, j and k and
    converts them to a 3 digit number in
    order k, j, i.

    >>> convert(4, 5, 6)
    '654'
    >>> convert(0, 1, 0)
    '10'

    '''
    if k == 0 and j == 0:
        return str(i)
    elif k == 0:
        return (str(j)+str(i))
    else:
        return (str(k)+str(j)+str(i))


def add_digits(n):
    '''(int) -> int

    Adds the digits of any 3 digit number, n.

    >>> add_digits(123)
    6
    >>> add_digits(456)
    15
        '''
    result = 0

    rem = n % 10
    result = result + rem
    n = int(n/10)
    rem = n % 10
    result = result + rem
    n = int(n/10)
    rem = n % 10
    result = result + rem
    n = int(n/10)

    return result


def add_digits2(n):
    '''(int) -> int

    Adds together the digits of a
    number, n, of any length.

    >>> add_digits(123)
    6
    >>> add_digits(6754837)
    40
    '''
    n = int(n)

    result = 0

    while n > 0:
        rem = n % 10
        result = result + rem
        n = int(n/10)
    return result


def profit(n):
    '''(num) -> float

    Returns the profit of a movie company
    based on the attendance, n. The profit is
    equal to the income from tickets, 5n, minus
    20, the cost of running the movie, and .5
    per person in attendance.

    >>> profit(6)
    7.0
    >>> profit(0)
    -20.0
    '''

	money = (5*n) - (20 + (.5*n))
	return money
