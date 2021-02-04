'''
CIS 210 Project 2-1: Determining Net Pay

Author: Cora Albers

Credits: N/A

Write a program to determine net pay based on inputs of number of hours
worked and gross pay.
'''



def tax(gross_pay):
    '''(num) -> float

    Takes in the amount of gross pay, n and computes
    15% of the gross pay to return the amount of tax.

    >>> tax(100)
    15.0
    >>> tax(500)
    75.0

    '''
    tax_to_pay = gross_pay * .15
    return tax_to_pay

def netpay(hours):
    '''(num) -> float

    Takes in the amount of hours worked and returns the
    amount of net pay after tax is removed.

    >>> netpay(1)
    9.56
    >>> netpay(40)
    382.5

    '''

    gross_pay = 11.25 * hours

    profit = gross_pay - tax(gross_pay)
    limited_profit = round(profit, 2)

    return limited_profit

def main():
    '''Net pay program driver.
    '''
    print('For 1 hours work, netpay is: ', netpay(1))
    print('For 40 hours work, netpay is: ', netpay(40))
    return None

main()
