'''
Author: Cora Albers

Credits: N/A

Description: A function that tests the correctness of the functions
sscount0 and sscount1
'''

import p34_sscount as p34


def test_sscount(f, args, expected_result):
    '''(function, str, int) -> None

    Tests a function, f, using arguments given in arguments
    to see if it will give the input expected result.

    >>> (sscount0, 'sses assesses', 2)
    testing sscount0
    Checking sses assesses
    its value 2 is correct!
    >>> (sscount0, 'needle haystack', 0)
    testing sscount0
    Checking needle haystack
    its value 0 is correct!
    >>> (sscount1, 'a a', 1)
    testing sscount1
    Checking a a
    its value 1 is correct!

    the strings ' abc' and ''  will not return the
    provided integer because in the first string, there
    are not two strings, and in the second, there
    is no string
    '''

    if args:
        space = args.index(' ')

        needle = args[: space]
        haystack = args[space+1 :]

        actual = f(needle, haystack)

        if actual == expected_result:
            print('testing ' + f.__name__)
            print('Checking ' + args)
            print('its value ' + str(actual) + ' is correct!')
        else:
            print('testing ' + f.__name__)
            print('Checking ' + args)
            print(str(actual) + ' is not correct.')

    elif not args:
        print('please enter a string to test')


    return None

def main():
    test_sscount(p34.sscount0, 'sses assesses', 2)
    test_sscount(p34.sscount0, 'an trans-Panamanian banana', 6)
    test_sscount(p34.sscount0, 'needle haystack', 0)
    test_sscount(p34.sscount0, '!!! !!!!!', 3)
    test_sscount(p34.sscount0, 'o pneumonoultramicroscopicsilicovolcanoconiosis', 9)
    test_sscount(p34.sscount0, '', 0)
    test_sscount(p34.sscount0, 'a ', 0)
    test_sscount(p34.sscount0,' abc', 0)
    test_sscount(p34.sscount0, 'a a', 1)
    test_sscount(p34.sscount1, 'sses assesses', 2)
    test_sscount(p34.sscount1, 'an trans-Panamanian banana', 6)
    test_sscount(p34.sscount1, 'needle haystack', 0)
    test_sscount(p34.sscount1, '!!! !!!!!', 3)
    test_sscount(p34.sscount1, 'o pneumonoultramicroscopicsilicovolcanoconiosis', 9)
    test_sscount(p34.sscount1, '', 0)
    test_sscount(p34.sscount1, 'a ', 0)
    test_sscount(p34.sscount1,' abc', 0)
    test_sscount(p34.sscount1, 'a a', 1)

    return None
