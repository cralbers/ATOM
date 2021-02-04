'''
CIS 210 Project 3-1: Fizzbuzz

Author: Cora Albers

Credits: N/A

Runs the fizzbuzz game on an input number.
'''

def fb(n):
    '''(int) -> None

    Prints fizz if n is divisible by 3, buzz if n is divisible
    by 5, fizzbuzz if n is divisible by both 3 and 5, and n if
    if is divisble by neither. Returns None.

    >>> fb(15)
    1
    2
    fizz
    4
    buzz
    fizz
    7
    8
    fizz
    buzz
    11
    fizz
    13
    14
    fizzbuzz

    >>> fb(1)
    1

    >>> fb(3)
    1
    2
    fizz
    '''

    for i in range(1, n+1):
        num = i % 3
        num2 = i % 5

        if (num == 0) and (num2 != 0) :
            print('fizz')
        elif (num2 == 0) and (num != 0):
            print('buzz')
        elif (num == 0) and (num2 == 0):
            print('fizzbuzz')\
        else:
            print(i)


    return None
