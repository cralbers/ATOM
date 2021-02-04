'''
Prior programming experience quiz.
CIS 210 Project 1-1 Hello-Quiz Solution

Author: Cora Albers

Credits: N/A

Add docstrings to Python functions that implement quiz 1 pseudocode.
(See p11_cricket.py for examples of functions with docstrings.)
'''

def q1(onTime, absent):
    '''(bool, bool) -> str

    Return response based on evaluation of onTime
    and absent as True or False:
    -if onTime is True -> 'Hello!'
    -if absent is True -> 'Is anyone there?'
    -if anything else -> 'Better late than never.'

    >>> q1(True, False)
    'Hello!'
    >>> q1(False, True)
    'Is anyone there?'
    '''
    if onTime:
        return('Hello!')
    elif absent:
        return('Is anyone there?')
    else:
        return('Better late than never.')

def q2(age, salary):
    '''(num, num) -> bool

    If the age is less than 18 and the
    salary is less than 10000 then the statement
    evaluates to True. If the age is less than
    18 or the salary greater than 10000 then the
    statement evaluates to False.

    >>> q2(13, 300)
    True
    >>> q2(19, 33333)
    False
    '''
    return (age < 18) and (salary < 10000)

def q3():
    '''(N/A) -> int

    Evaluates the values of p and q and then
    determines if p is less than q. Will always
    return 6 because there are no conditionals
    of the function.

    >>> q3()
    6

    '''
    p = 1
    q = 2
    result = 4
    if p < q:
        if q > 4:
            result = 5
        else:
            result = 6

    return result

def q4(balance, deposit):
    '''(num, num) -> num

    The deposit value is added 10 times to
    the value of the balance.

    >>> q4(13, 13)
    143
    >>> q4(15, 1)
    25
    '''
    count = 0
    while count < 10:
        balance = balance + deposit
        count += 1

    return balance

def q5(nums):
    '''(list of numbers) -> int    #fill in the rest of the type contract

    While i is less than the number of numbers
    in the list, the function will add 1 to the
    value of result if the list value being
    examined is greater than or equal to 0.

    >>> q5([0, 1, 2, 3, 4, 5])    #examples are given
    6
    >>> q5([0, -1, 2, -3, 4, -5])
    3
    '''
    result = 0
    i = 0
    while i < len(nums):
        if nums[i] >= 0:
            result += 1

        i += 1

    return result

def q6():
    '''(N/A) -> int

    No result will return because at the beginning
    of every loop, the i value reevaluates to 1.
    The loop will run until stopped manually.

    >>> q6()

    >>> q6()

    '''
    i = 0
    p = 1
    while i < 4:
        i = 1
        p = p * 2
        i += 1

    return p
