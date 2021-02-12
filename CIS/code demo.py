'''An old-style movie theatre has a simple profit function.
Each customer pays $5 per ticket. Each performance costs
the theatre $20, plus .50 per attendee. Write a function,
profit, which returns the net profit per show, given the
number of attendees at the show. (Python Variations, from
How to Design Programs, Felleisen, et al.)'''

'''
CIS 210 Code Demo

Author: Cora Albers

An old-style movie theatre has a simple profit function.
Each customer pays $5 per ticket. Each performance costs
the theatre $20, plus .50 per attendee. Write a function,
profit, which returns the net profit per show, given the
number of attendees at the show. (Python Variations, from
How to Design Programs, Felleisen, et al.)
'''

import doctest

def profit(attendees):
    '''(int) -> float

    Given the number of attendees, return the net profit of a theatre
    where each attendant pays $5, and it costs the theatre $20 per show,
    and .50 per attendee.

    >>> profit(5)
    2.5
    >>> profit(0)
    -20.0
    >>> profit(3)
    -6.5
    '''

    TICKET = 5
    ATTENDEE_COST = .5


    income = TICKET * attendees

    cost = 20 + (attendees * ATTENDEE_COST)

    net_profit= income - cost

    return net_profit


print(doctest.testmod())
