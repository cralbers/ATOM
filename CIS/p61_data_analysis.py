'''
CIS 210 Project 6-2: Data Analysis

Author: Cora Albers

Credits:

Description:

'''

def mean(aList):
    '''
    '''
    mean = sum(aList) / len(aList)
    return mean


def median(aList):
    copyList = aList[:]
    copyList.sort()
    if len(copyList) % 2 == 0:
        rightMid = len(copyList) // 2
        leftMid = rightMid - 1
        median = (cop)
