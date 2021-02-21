'''
More Automated Testing and Debugging
CIS 210 Project 6-2 Winter 2021

Author: Cora Albers

Credits: N/A

Functions need to be tested and debugged;
write a function to automate testing of calendar function (project 5-1)
'''
import doctest
import p51_printcal as p51

def bigSalesBug(sales_list):
    '''(list) -> number

    Returns sum of all sales for amounts at or over $40,000.
    sales_list has the record of all the sales.

    >>> bigSalesBug([40000, 45.67, 19000.0, 25000, 100000])
    140000.0
    >>> bigSalesBug([4, 3, 2, 1])
    0.0
    >>> bigSalesBug([0])
    0.0
    >>> bigSalesBug([54000, 32000, 1000])
    54000.0
    '''
    total = 0.00
    for sales in sales_list: #inserted colon
        if sales >= 40_000: #inserted colon and greater than or equal to sign
            total = total + sales #fixed typo from tottal to total
    return total #decreased indent

############

def findRangeBug(salesli):
    '''(list) -> tuple

    Returns largest and smallest number in non-empty salesli.
    (Note that Python has built in funcs max and min
    to do this, but not using them here, so we can
    work with the list directly.)

    >>> findRangeBug([40000, 45.67, 19000.0, 25000, 100000])
    (45.67, 100000.0)
    >>> findRangeBug([5, 4, 3, 2, 1])
    (1.0, 5.0)
    >>> findRangeBug([0])
    (0.0, 0.0)
    >>> findRangeBug([1, 1])
    (1.0, 1.0)
    '''
    salesli.sort() #cannot reassign variable, because .sort returns None
    low = float(salesli[0])
    high = float(salesli[-1])
    return low, high

def salesReportBug(salesli):
    '''(list) --> None

    Prints report of sales totals for each day of week (salesli)
    and range of per-day sales. salesli is non-empty - 0 sales
    for any day are reported as 0.

    > salesReportBug([40000, 45.67, 19000.0, 25000, 100000])
    Weekly Range: $45.67 - $100,000.00

    Mon          Tue          Wed          Thu          Fri
    $40,000.00   $45.67       $19,000.00   $25,000.00   $100,000.00
    > salesReportBug([0,0,0,0,0])
    Weekly Range: $0.00 - $0.00

    Mon          Tue          Wed          Thu          Fri
    $0.00        $0.00        $0.00        $0.00        $0.00
    > salesReportBug([5, 4, 3, 2, 1])
    Weekly Range: $1.00 - $5.00

    Mon          Tue          Wed          Thu          Fri
    $5.00        $4.00        $3.00        $2.00        $1.00
    > salesReportBug([0])
    Weekly Range: $0.00 - $0.00

    Mon          Tue          Wed          Thu          Fri
    $0.00        $0.00        $0.00        $0.00        $0.00
    '''
    if salesli == []:
        salesli = [0,0,0,0,0]
    elif salesli == [0]:
        salesli = [0,0,0,0,0]
    #generates a copy of salesli
    copysalesli = salesli.copy()

    #calculate and report low and high sales
    low, high = findRangeBug(salesli)
    print(f'Weekly Range: ${low:,.2f} - ${high:,.2f}\n')

    #print daily report header
    fw = 12
    print(f"{'Mon':<{fw}} {'Tue':<{fw}} {'Wed':<{fw}} {'Thu':<{fw}} {'Fri':<{fw}}")



    #report on sales per day from list data
    for sales in copysalesli:
        print(f'${float(sales):<{fw},.2f}', end='')

    return None

def test_calendar():
    '''(N/A) -> None

    Runs the calendar function on a list of 6 tuple test cases to test
    the functionality of calendar.

    >>> test_calendar()
    Feb 2021
    Su Mo Tu We Th Fr Sa
        1  2  3  4  5  6
     7  8  9 10 11 12 13
    14 15 16 17 18 19 20
    21 22 23 24 25 26 27
    28
    Aug 2021
    Su Mo Tu We Th Fr Sa
     1  2  3  4  5  6  7
     8  9 10 11 12 13 14
    15 16 17 18 19 20 21
    22 23 24 25 26 27 28
    29 30 31
    Jan 2022
    Su Mo Tu We Th Fr Sa
                       1
     2  3  4  5  6  7  8
     9 10 11 12 13 14 15
    16 17 18 19 20 21 22
    23 24 25 26 27 28 29
    30 31
    Jan 2020
    Su Mo Tu We Th Fr Sa
              1  2  3  4
     5  6  7  8  9 10 11
    12 13 14 15 16 17 18
    19 20 21 22 23 24 25
    26 27 28 29 30 31
    Apr 2030
    Su Mo Tu We Th Fr Sa
        1  2  3  4  5  6
     7  8  9 10 11 12 13
    14 15 16 17 18 19 20
    21 22 23 24 25 26 27
    28 29 30
    Dec 2050
    Su Mo Tu We Th Fr Sa
                 1  2  3
     4  5  6  7  8  9 10
    11 12 13 14 15 16 17
    18 19 20 21 22 23 24
    25 26 27 28 29 30 31

    '''
    calendar_tests = [(2, 2021), (8, 2021), (1, 2022), (1, 2020), (4, 2030), (12, 2050)]
    # test function explanations: 1st tests current time, 2nd tests for formatting of a
    # month that starts on a Sunday, 3rd tests for previous years, 4th tests for future
    # years, 5th tests for new decade, 6th tests general formatting

    for i in calendar_tests:
        p51.calendar(i[0], i[-1])

    return None

print(doctest.testmod())
