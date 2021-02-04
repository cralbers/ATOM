'''
Testing and debugging
CIS 210 Project 4-2 Winter 2021

Author: Cora Albers

Credits: N/A

Functions need to be tested.
'''
import doctest

def ratsBug(weight, rate):
    '''(number, number) -> tuple

    Return number of weeks it will
    take for a rat to weigh 1.5 times
    as much as its original weight
    (weight > 0) if it gains at rate (rate > 0).

    >>> ratsBug(10, .1)     # normal
    (16.1, 5)
    >>> ratsBug(1, .5)      # edge - just one week
    (1.5, 1)
    >>> ratsBug(10, .9)
    (19.0, 1)
    >>> ratsBug(8, .01)
    (12.0, 41)
    >>> ratsBug(5, .2)
    (8.6, 3)
    '''
    wks = 0
    goalWeight = weight * 1.5
    while weight < goalWeight:
        weight += weight * rate
        wks = wks + 1

    weight = round(weight, 1)
    return (weight, wks)

def countSeqBug(astr):
    '''(str) -> int

    Returns the length of the longest recurring
    sequence in astr

    >>> countSeqBug('abccde')  # normal
    2
    >>> countSeqBug('')        # edge - empty string
    0
    >>> countSeqBug('ffahhh')
    3
    >>> countSeqBug('mother')
    1
    >>> countSeqBug('  ')      # 2 spaces
    2
    '''
    if len(astr) != 0:
        prev_item = astr[0]
        dup_ct = 1
        high_ct = 1
    else:
        high_ct = 0
        dup_ct = 0

    for i in range(1, len(astr)):
        if astr[i] == prev_item:
            dup_ct += 1
            if dup_ct > high_ct:
                high_ct = dup_ct
        else:
            prev_item = astr[i]

            if dup_ct > high_ct:
                high_ct = dup_ct
            dup_ct = 1

    return high_ct

def my_averageBug(dataset):
    '''(str) -> float

    Returns average of values in input string values,
    but zeros do not count at all.  Return 0 if there
    is no real data.

    >>> my_averageBug('23')    #normal, no zeros
    2.5
    >>> my_averageBug('203')   #normal, a zero
    2.5
    >>> my_averageBug('0000')  #all zeros
    0
    >>> my_averageBug('1')     #single item string
    1.0
    >>> my_averageBug('05050505')
    5.0
    >>> my_averageBug('2003')
    2.5
    >>> my_averageBug('0009')
    9.0
    >>> my_averageBug('543')
    4.0
    '''
    count = 0
    total = 0
    for value in dataset:
        if value != '0':
            total += int(value)
 # use int to change string to integer
            count += 1
    if count != 0:
        avg = total / count
    else:
        avg = 0

    return avg

print(doctest.testmod())
