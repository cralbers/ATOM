'''
CIS 210 Project 5-2: Parity Bit

Author: Cora Albers

Credits: N/A

Description: Adds a parity bit to individual characters in a sequence,
checks the parity bit for each character, and then reports any errors.
'''
def encode(letter):
    '''(str) -> str

    Adds a parity bit to the binary of the input letter.

    >>> encode('a')
    '11100001'
    >>> encode('b')
    '11100010'
    >>> encode('c')
    '01100011'
    >>> encode('d')
    '11100100'
    '''
    #converts letter to binary
    binNum = bin(ord(letter))

    # runs parity on binary number to determine parity bit and adds it to
    # the binary number sequence
    return (parity(binNum) + binNum[2:])

def parity(bitrep):
    '''(str) -> str

    Determines the one character string parity bit for an input binary
    string, bitrep.

    >>> parity('1100011')
    '0'
    >>> parity('1100100')
    '1'
    '''
    counter = 0
    for num in bitrep:
        if num == '1':
            counter = counter + 1
    remainder = counter % 2
    if remainder == 1:
        return '1'
    elif remainder == 0:
        return '0'


def decode(pletter):
    ''' (str) -> str

    Given a binary string, pletter, determines if the number of 1's is
    even, meaning that the parity is functioning correctly. Then either
    indicates an error or returns the character encoded by pletter.

    >>> decode('01100011')
    'c'
    >>> decode('11100100')
    'd'

    '''
    check = parity(pletter)
    counter = 0
    for num in check:
        if num == '1':
            counter = counter + 1
    remainder = counter % 2

    if remainder == 1:
        return '*'
    if remainder == 0:
        pletter = pletter[1:]
        return (chr(int(pletter, 2)))

def main():
    word = 'chips'
    for letter in word:
        print(decode(encode(letter)),end='')
    print()

if __name__ == '__main__':
    main()
