import doctest

def double_your_num():
    x = int(input('enter a number between 1 and 10: '))
    try:
        assert x <= 10 and x >= 1
    except
    
    print(f'the result is {x*2}')


def incr_li(li, n):
    '''(list of ints, int) -> None

    Increment the first n values in a list by 1 and print the new list.

    >>> incr_li([1, 2, 3, 4], 2)
    [2, 3, 3, 4]

    >>> incr_li([1, 2, 3, 4], 5)
    [2, 3, 4, 5]
    '''
    newli = li [:]
    for i in range(n):
        newli[i] += 1
    print(newli)

    return None
    
