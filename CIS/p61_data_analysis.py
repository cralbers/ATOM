'''
CIS 210 Project 6-2: Data Analysis

Author: Cora Albers

Credits: N/A

Description: Implement functions that analyze numerical data.

'''

import doctest
equakes = [5.3, 3.0, 2.6, 4.4, 2.9, 4.8, 4.3,
2.6, 2.9, 4.9, 2.5, 4.8, 4.2, 2.6,
4.8, 2.7, 5.0, 2.7, 2.8, 4.3, 3.1,
4.1, 2.8, 5.8, 2.5, 3.9, 4.8, 2.9,
2.5, 4.9, 5.0, 2.5, 3.2, 2.6, 2.7,
4.8, 4.1, 5.1, 4.7, 2.6, 2.9, 2.7,
3.3, 3.0, 4.4, 2.7, 5.7, 2.5, 5.1,
2.5, 4.4, 4.6, 5.7, 4.5, 4.7, 5.1,
2.9, 3.3, 2.7, 2.8, 2.9, 2.6, 5.3,
6.0, 3.0, 5.3, 2.7, 4.3, 5.4, 4.4,
2.6, 2.8, 4.4, 4.3, 4.7, 3.3, 4.0,
2.5, 4.9, 4.9, 2.5, 4.8, 3.1, 4.9,
4.4, 6.6, 3.3, 2.5, 5.0, 4.8, 2.5,
4.2, 4.5, 2.6, 4.0, 3.3, 3.1, 2.6,
2.7, 2.9, 2.7, 2.9, 3.3, 2.8, 3.1,
2.5, 4.3, 3.2, 4.6, 2.8, 4.8, 5.1,
2.7, 2.6, 3.1, 2.9, 4.2, 4.8, 2.5,
4.5, 4.5, 2.8, 4.7, 4.6, 4.6, 5.1,
4.2, 2.8, 2.5, 4.5, 4.6, 2.6, 5.0,
2.8, 2.9, 2.7, 3.1, 2.6, 2.5, 3.2,
3.2, 5.2, 2.8, 3.2, 2.6, 5.3, 5.5,
2.7, 5.2, 6.4, 4.2, 3.1, 2.8, 4.5,
2.9, 3.1, 4.3, 4.9, 5.2, 2.6, 6.7,
2.7, 4.9, 3.0, 4.9, 4.7, 2.6, 4.6,
2.5, 3.2, 2.7, 6.2, 4.0, 4.6, 4.9,
2.5, 5.1, 3.3, 2.5, 4.7, 2.5, 4.1,
3.1, 4.6, 2.8, 3.1, 6.3]

def isEven(n):
    ''' (int) -> bool

    Returns boolean value based on whether input n is even or odd.

    >>> isEven(5)
    False
    >>> isEven(2)
    True
    >>> isEven(0)
    True
    '''
    if n % 2 == 0:
        return True
    else:
        return False

def mean(aList):
    ''' (list) -> float

    Adds together and then averages an input list of numbers, aList.

    >>> mean([1, 2, 3, 4, 5, 4, 3, 2, 1])
    2.7777777777777777
    >>> mean([0])
    0.0
    >>> mean([99, 4, 1, 2, 54, 12])
    28.666666666666668
    '''
    mean = sum(aList) / len(aList)
    return mean


def median(aList):
    ''' (list) -> num

    Given an input list of numbers, aList, orders them from least to
    greatest, and then returns the middle value.

    >>> median([1, 2, 3, 4, 5, 4, 3, 2, 1])
    3
    >>> median([4, 4, 4, 4, 4])
    4
    >>> median([99, 4, 1, 2, 54, 12])
    8.0
    '''
    copyList = aList[:]
    copyList.sort()
    if isEven(len(copyList)) == True: #even length
        rightMid = len(copyList) // 2
        leftMid = rightMid - 1
        median = (copyList[leftMid] + copyList[rightMid]) / 2
    else: #odd length
        mid = len(copyList) // 2
        median = copyList[mid]
    return median

def mode(aList):
    ''' (list) -> list

    Given an input list of numbers, aList, returns the value that appears
    the greatest number of times.

    >>> mode([1, 2, 4, 7, 6, 3, 2, 1, 1, 8])
    [1]
    >>> mode([1, 2, 3, 4, 5])
    [1, 2, 3, 4, 5]
    >>> mode([3, 4, 9, 19, 19])
    [19]
    '''
    countDict = genFrequencyTable(aList)

    countList = countDict.values()
    maxCount = max(countList)

    modeList = []
    for item in countDict:
        if countDict[item] == maxCount:
            modeList.append(item)


    return modeList

def frequencyTable(aList):
    ''' (list) -> str

    Given an input list of values, aList, outputs a table that
    displays the number of times a certain number appears
    in the list.

    > frequencyTable([1, 3, 3, 2])
    ITEM FREQUENCY
    1    1
    2    1
    3    2
    > frequencyTable([2, 3, 3, 6, 8, 8])
    ITEM FREQUENCY
    2       1
    3       2
    6       1
    8       2
    '''
    countDict = genFrequencyTable(aList)

    itemList = list(countDict.keys())
    itemList.sort()

    print('ITEM', 'FREQUENCY')

    for item in itemList:
        print(item, '     ', countDict[item])


def genFrequencyTable(aList):
    ''' (list) -> dict

    Given a list, aList, returns a dictionary with integers as keys, and
    the frequency of the integer as the values.

    >>> genFrequencyTable([1, 2, 3, 3, 1, 4, 5])
    {1: 2, 2: 1, 3: 2, 4: 1, 5: 1}
    >>> genFrequencyTable([1, 2, 3, 1, 2, 3, 4, 6])
    {1: 2, 2: 2, 3: 2, 4: 1, 6: 1}
    >>> genFrequencyTable([0])
    {0: 1}
    '''
    countDict = {}

    for item in aList:
        if item in countDict:
            countDict[item] = countDict[item] + 1
        else:
            countDict[item] = 1

    return countDict

def main(aList):
    mean_result = mean(aList)
    median_result = median(aList)
    mode_result = mode(aList)

    mode_result = mode_result[0]

    print('The mean is ', mean_result)
    print('The median is ', median_result)
    print('The mode is ', mode_result)
    frequencyTable(aList)


if __name__ == '__main__':
    main(equakes)



print(doctest.testmod())
