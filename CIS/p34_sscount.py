'''
CIS 210 Project 3-4: Python Strings/Counting

Author: Cora Albers

Credits: N/A

Assemble a function to count the number of times a substring
appears in a string.
'''

import doctest

def sscount0(needle, haystack):
    '''(str, str) -> int

    Takes in two strings, needle and haystack, and counts the number
    of times that the needle string appears in the haystack string.

    >>> sscount0('sses', 'assesses')
    2
    >>> sscount0('!!!', '!!!!!')
    3
    >>> sscount0('iss', 'mississippi')
    2
    >>> sscount1('..', '.....')
    4
    '''

    count = 0

    for i in range(len(haystack)):
        x = len(needle)

        if haystack[i : i + x] == needle:
            count = count + 1
        else:
            pass

    return count

def sscount1(needle, haystack):
    '''(str, str) -> int

    Takes in two strings, needle and haystack, and counts the number
    of times that the needle string appears in the haystack string.

    >>> sscount0('sses', 'assesses')
    2
    >>> sscount0('!!!', '!!!!!')
    3
    >>> sscount0('iss', 'mississippi')
    2
    >>> sscount1('..', '.....')
    4
    '''

    count = 0
    for i in range(len(haystack)):
        if haystack[i:].startswith(needle):
            count = count + 1
        else:
            pass

    return count

#print(doctest.testmod())
