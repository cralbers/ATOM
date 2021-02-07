'''
CIS 210 Project 5-1: Calendar

Name: Cora Albers

Credits:

Description: Prints a calendar given an input month and year.
'''

import datetime


def calendar(month, year):
    '''(int, int) -> calendar

    Given an input month and year, prints a calendar with weekdays
    in format

    Month Year
    Su Mo Tu We Th Fr Sa
              1  2  3  4
     5  6  7  8  9 10 11
    12 13 14 15 16 17 18
    19 20 21 22 23 24 25
    26 27 28 29 30

    >>> calendar(8, 2021)
    Aug 2021
    Su Mo Tu We Th Fr Sa
     1  2  3  4  5  6  7
     8  9 10 11 12 13 14
    15 16 17 18 19 20 21
    22 23 24 25 26 27 28
    29 30 31
    >>> calendar(2, 2020)
    Feb 2020
    Su Mo Tu We Th Fr Sa
                       1
     2  3  4  5  6  7  8
     9 10 11 12 13 14 15
    16 17 18 19 20 21 22
    23 24 25 26 27 28
    >>> calendar(10, 2019)
    Oct 2019
    Su Mo Tu We Th Fr Sa
           1  2  3  4  5
     6  7  8  9 10 11 12
    13 14 15 16 17 18 19
    20 21 22 23 24 25 26
    27 28 29 30 31
    '''

    #random assignment tuples
    MONTHS_DAYS = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    MONTHS_NAMES = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
    WEEKDAYS = ('Su', 'Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa')

    #determine and assign start day
    adate = datetime.date(year, month, 1)
    # M = 1, TU = 2, W = 3, TH = 4, F = 5, SA = 6, SU = 7 EU
    # M = 2, TU = 3, W = 4, TH = 5, F = 6, SA = 7, SU = 1 US
    startday = adate.isoweekday()

    #first line of dates code shit
    numDays = MONTHS_DAYS[month - 1]

    #title line
    monthTitle = MONTHS_NAMES[month - 1]
    titleLine = '{:<20}'.format(monthTitle + ' ' + str(year))
    print(titleLine)

    #weekdays title line
    counter = 0
    for day in WEEKDAYS:
        print('{:<3}'.format(day), end='')
        counter = counter + 1
        if counter == 7:
            print()
            counter = 0

    #aligns cursor for first line and prints dates
    if startday <= 6:
        print('{:<3}'.format('') * (startday), end='')
        endOfWeek = startday
        for day in range(1, numDays + 1):
            print('{:>2}'.format(day), end='')
            endOfWeek = endOfWeek + 1
            print(' ', end='')
            if endOfWeek == 7:
                print()
                endOfWeek = 0
    if startday == 7:
        endOfWeek = 0
        for day in range(1, numDays + 1):
            print('{:>2}'.format(day), end='')
            endOfWeek = endOfWeek + 1
            print(' ', end='')
            if endOfWeek == 7:
                print()
                endOfWeek = 0
    print()

def main(year):
    '''(int) -> calendar
    '''
    for i in range(1, 13):
        calendar(i, year)

if __name__ == '__main__':
    main(2021)
