'''
CIS 210 Project 7-1: Who takes CIS 210?
Author: Cora Albers
Credits: N/A
Description: Analyzes a text file containing data on majors enrolled in
CIS 210.
'''
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
        print('{:<10}'.format(item), countDict[item])

def majors_readf(fname):
    ''' (str) -> list

    Returns a list of the text contained in the text file, fname.

    >>> majors_readf('majors-short.txt')
    ['PHYS', 'PSY', 'CIS', 'PBA', 'CIS', 'JMS', 'BI', 'BI', 'PDS', 'SDSC', 'CIS', 'ARCH', 'PHYS', 'EXPL', 'MACS', 'CIS', 'PBA', 'BADM', 'CIS', 'CIS']
    '''
    with open(fname, 'r') as readf:

        line = readf.readline() # get past title line
        line = readf.readline() # get past title line
        majorsListAll = []

        for line in readf:
            line = line.strip() # remove new line lingo
            majorsListAll.append(line)
    return majorsListAll

def majors_analysis(majorsli):
    ''' (list) -> tuple

    Returns a tuple of the most frequently occuring majors and the
    number of distinct majors in the list, majorsli.

    >>> majors_analysis(['CIS', 'CIS', 'EXPL', 'COLT', 'EXPL'])
    (['CIS', 'EXPL'], 3)
    '''
    # this is the counter for number of majors in the list
    counter = 0
    majorsList=[]
    for i in majorsli:
        if i not in majorsList:
            majorsList.append(i)
            counter = counter + 1

    # this is the part to get mode of data
    countDict = genFrequencyTable(majorsli)

    countList = countDict.values()
    maxCount = max(countList)

    modeList = []
    for item in countDict:
        if countDict[item] == maxCount:
            modeList.append(item)

    return_tuple = (modeList, counter)
    return return_tuple

def majors_report(majors_mode, majors_ct, majorsli):
    '''(list, int, list) -> str? shit idk

    Generates a readable report of majors data using auxiliary functions.

    >>> majors_report(['CIS', 'EXPL'], 3, ['CIS', 'CIS', 'EXPL',
    'COLT', 'EXPL'])
    3 majors are represented in CIS 210 this term.
    The most represented major(s): CIS EXPL
    ITEM FREQUENCY
    CIS     2
    COLT    1
    EXPL    2
    '''
    majors_mode = ' ,'.join(majors_mode)
    print(majors_ct, 'majors are represented in CIS 210 this term.')
    print('The most represented major(s) are: ', majors_mode)
    frequencyTable(majorsli)

def main():
    '''()-> None
    Calls: majors_readf, majors_analysis, majors_report
    Top level function for analysis of CIS 210 majors data.
    '''
    #fname = 'majors-short.txt'
    fname = 'p71-majors-cis210W20.txt'

    majorsli = majors_readf(fname) #read
    majors_mode, majors_ct = majors_analysis(majorsli) #analyze
    majors_report(majors_mode, majors_ct, majorsli) #report
    return None

if __name__ == '__main__':
    main()
