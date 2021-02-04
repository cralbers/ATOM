'''
CIS 210 Project 2-0: Learning Looping

Author: Cora Albers

Credits: N/A

Revise and implement functions from Project 1.2 using for loops.
'''


def q6_better():
    '''(N/A) -> int

    No result will return because at the beginning
    of every loop, the i value reevaluates to 1.
    The loop will run 4 times.

    >>> q6()

    >>> q6()

    '''
    i = 0
    p = 1
    for i in range(4):
        i = 1
        p = p * 2
        i += 1

    return p


def q6_final(n, m):
    '''(int, int) -> int

    Returns the value of n raised to the power of m.

    >>> (3, 3)
    27

    >>> (4, 2)
    16
    '''
    power = 1

    for i in range(1, m+1):
        power = power * n

    return power


def add_digits2a_better(n):
    '''(int) -> int

    Return the sum of a 3 digit integer, n.
    Implement using a for loop.

    >>> add_digits2a_better(123)
    6

    >>> add_digits2a_better(456)
    15

    '''

    digit_sum = 0
    ctr = 1

    for i in range(3):
        digit = n % 10
        n = n // 10
        digit_sum += digit
        ctr += 1

    return digit_sum
