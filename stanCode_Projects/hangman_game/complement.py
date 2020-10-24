"""
Name: Pei-Feng (Kevin) Ma
File: complement.py
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program asks uses for a DNA sequence as
a python string that is case-insensitive.
Your job is to output the complement of it.
"""


def main():
    """
    This program will receive a DNS sequence and return a complement sequence.
    'A' matches to 'T' and 'C' matches to 'G'.
    1. create a string 'DNA' receive user's DNA input.
    2. make string dna case insensitive.
    3. create a function 'com' to return a complement of user's dna string
    4. print out 'dna' and 'com(dna)'
    """
    dna = str(input('Please give me a DNA strand and I\'ll find the complement: '))
    dna = dna.upper()
    print('The complement of '+str(dna)+' is '+str(com(dna)))


def com(n):
    """
    This function will return the complement DNA of user's input DNA
    :param n: str, DNA string input by user
    :return: str, the complement DNA of user's input
    """
    dna = ''
    for ch in n:
        if ch == 'A':
            dna += 'T'
        elif ch == 'T':
            dna += 'A'
        elif ch == 'C':
            dna += 'G'
        else:
            dna += 'C'
    return dna



###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
