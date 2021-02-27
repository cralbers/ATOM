'''
CIS 210 Project 7-2: Earthquake Watch
Author: Cora Albers

'''
import p61_data_analysis as p61

def equake_readf(fname):
    ''' (str) -> list

    Returns a list of all of the earthquak magnitudes in a file, fname.

    >>> equake_readf('p72-equakes-50f-2019.csv')
    [5.2, 5.1, 6.0, 5.9, 5.6, 5.7, 5.0, 5.0, 5.2, 5.1, 5.4, 5.2, 5.6, 5.18, 5.1, 5.0, 5.0, 5.6]
    '''
    with open(fname, 'r') as readf:
        line = readf.readline() # get past title line
        magsAll = []

        for line in readf:
            value = line.strip().split(',') # remove new line lingo
            magsAll.append(float(value[4]))

    return magsAll

def equake_analysis(magnitudes):
    ''' (list) -> tuple

    Returns a tuple of mean, median and mode of the list, magnitudes.

    >>> equake_analysis(equake_readf(fname))
    (5.326666666666666, 5.2, [5.0])
    '''

    mean_result = p61.mean(magnitudes)
    median_result = p61.median(magnitudes)
    mode_result = p61.mode(magnitudes)

    return_tuple = (mean_result, median_result, mode_result)

    return return_tuple

def equake_report(magnitudes, mmm, minmag):
    ''' (list, tuple, int) -> str

    Generates a readable report of earthquake magnitudes using
    auxiliary functions.

    >>> equake_report(equake_readf(fname), equake_analysis(magnitudes), minmag)
    There have been 18 earthquakes with magnitude 5.0 or higher.

    Mean magnitude is: 5.326666666666666
    Median magnitude is: 5.2
    Mode(s) of magnitudes is: 5.0

    ITEM FREQUENCY
    5.0       4
    5.1       3
    5.18       1
    5.2       3
    5.4       1
    5.6       3
    5.7       1
    5.9       1
    6.0       1
    '''
    abovemin = []
    for mag in magnitudes:
        if mag >= minmag:
            abovemin.append(mag)


    num_equakes = len(abovemin)
    mode = []
    for i in mmm[2]:
        str_num = str(i)
        mode.append(str_num)

    mode = ' ,'.join(mode)


    print('There have been', num_equakes, 'earthquakes with magnitude', minmag,
    'or higher.\n')
    print('Mean magnitude is:', mmm[0])
    print('Median magnitude is:', mmm[1])
    print('Mode(s) of magnitudes is:', mode, '\n')
    p61.frequencyTable(abovemin)

    return None

def main():
    '''()-> None
    Calls: equake_readf, equake_analysis, equake_report
    Top level function for earthquake data analysis.
    Returns None.
    '''
    fname = 'p72-equakes-25f-2019.csv'
    minmag = 2.5
    #fname = 'p72-equakes-50f-2019.csv'
    #minmag = 5.0
    emags = equake_readf(fname)
    mmm = equake_analysis(emags)
    equake_report(emags, mmm, minmag)
    return None

if __name__ == '__main__':
    main()
