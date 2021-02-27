'''
CIS 210 Midterm
Author: Cora Albers
Credits: N/A
Description: Defines a function that given a text file, determines which
west coast state has full vaccinated the largest percent of its population.
'''

def who_is_winning(fname):
    '''(str) -> str

    Determines using a text file of data which state has the highest percent
    of its population vaccinated.

    >>> who_is_winning('covid_19.txt')
    Oregon is winning
    '''
    with open(fname, 'r') as readf:
        line = readf.readline()
        line = readf.readline()
        line = readf.readline()

        states = []
        two_doses = []
        percent_vaccinated = []
        for line in readf:
            value = line.strip().split(' ') # remove new line lingo
            two_doses.append(value[5])
            states.append(value[0])
            percent_vaccinated.append((int(value[5]) / int(value[1]))*100)

        max_index = percent_vaccinated.index(max(percent_vaccinated))
        state = states[max_index]

        winning_statement = (f'{state} is winning')
        print(winning_statement)
